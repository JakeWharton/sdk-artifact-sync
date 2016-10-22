#!/usr/bin/python -u

"""
Copyright 2016 Jake Wharton

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import argparse
import os
import subprocess
import sys
import urllib2

__version__ = '1.0.0'

sdk = os.environ['ANDROID_HOME']

parser = argparse.ArgumentParser(description='Synchronize SDK artifacts with a remote Maven repo')
parser.add_argument('--sdk', dest='sdk', help='Path to Android SDK. Defaults to ANDROID_HOME.')
parser.add_argument('--dry-run', dest='dry_run', action='store_true', help='Prepare sync but do not execute.')
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Print verbose logging.')
parser.add_argument('repo_id', help='Remote repository ID (for authentication via settings.xml).')
parser.add_argument('repo_url', help='Remote repository URL.')
args = parser.parse_args()


repo_id = args.repo_id
repo_url = args.repo_url
if not repo_url.endswith('/'):
    repo_url += '/'
if args.sdk is not None:
    sdk = args.sdk
dry_run = args.dry_run or False
verbose = args.verbose or False

if verbose:
    print 'Repository ID: %s' % repo_id
    print 'Repository URL: %s' % repo_url
    print 'Android SDK: %s' % sdk

if dry_run:
    print 'Dry run! No artifacts will be uploaded.'
    print
elif verbose:
    print 'Dry run: %s' % dry_run
    print

sdk_extras = os.path.join(sdk, 'extras')
sdk_m2_repos = [
    os.path.join(sdk_extras, 'android', 'm2repository'),
    os.path.join(sdk_extras, 'google', 'm2repository'),
    os.path.join(sdk_extras, 'm2repository')
]
if verbose:
    print 'Potential SDK m2repository folders:\n  %s' % '\n  '.join(sdk_m2_repos)

sdk_m2_repos = filter(lambda x: os.path.exists(x), sdk_m2_repos)
if len(sdk_m2_repos) == 0:
    print 'No m2repositories found in SDK extras at %s' % sdk_extras
    sys.exit(1)
if verbose:
    print 'Actual SDK m2repository folders:\n  %s' % '\n  '.join(sdk_m2_repos)

sdk_artifacts = []
for sdk_m2_repo in sdk_m2_repos:
    for dir_path, _, file_names in os.walk(sdk_m2_repo):
        for file_name in file_names:
            artifact_name, ext = os.path.splitext(file_name)
            if (ext == '.aar' or ext == '.jar') \
                    and not artifact_name.endswith('-sources') \
                    and not artifact_name.endswith('-javadoc'):
                artifact_file = os.path.join(dir_path, file_name)
                relative_file = os.path.relpath(artifact_file, sdk_m2_repo)
                artifact = {
                    'file': artifact_file,
                    'relative_file': relative_file,
                    'pom': os.path.join(dir_path, artifact_name + '.pom'),
                }

                artifact_sources = os.path.join(dir_path, artifact_name + '-sources.jar')
                has_sources = os.path.exists(artifact_sources)
                if has_sources:
                    artifact['sources'] = artifact_sources

                artifact_javadoc = os.path.join(dir_path, artifact_name + '-javadoc.jar')
                has_javadoc = os.path.exists(artifact_javadoc)
                if has_javadoc:
                    artifact['javadoc'] = artifact_javadoc

                sdk_artifacts.append(artifact)

                if verbose:
                    print 'Found %s' % relative_file
                    print '  Repo: %s' % sdk_m2_repo
                    print '  Sources: %s' % has_sources
                    print '  Javadoc: %s' % has_javadoc
                else:
                    print '\rLoading %s artifacts from your local SDK...' % len(sdk_artifacts),

print '\rLoaded %s artifacts from your local SDK.            ' % len(sdk_artifacts)
if verbose:
    print


class HeadRequest(urllib2.Request):
    def get_method(self):
        return 'HEAD'


missing_artifacts = []
for index, sdk_artifact in enumerate(sdk_artifacts):
    relative_file = sdk_artifact['relative_file']
    if verbose:
        print '[%s/%s] Checking %s...' % (index + 1, len(sdk_artifacts), relative_file),
    else:
        print '\rChecking %s of %s artifacts on remote...' % (index + 1, len(sdk_artifacts)),
    try:
        if urllib2.urlopen(HeadRequest(repo_url + relative_file)).getcode() == 200:
            if verbose:
                print 'Found!'
            continue
    except urllib2.HTTPError:
        pass
    if verbose:
        print 'Missing!'
    missing_artifacts.append(sdk_artifact)

print '\r%s of %s artifacts missing from remote.            ' % (len(missing_artifacts), len(sdk_artifacts))
if verbose:
    print


for index, missing_artifact in enumerate(missing_artifacts):
    cmd = [
        'mvn',
        'deploy:deploy-file',
        '-DrepositoryId=' + repo_id,
        '-Durl=' + repo_url,
        '-Dfile=' + missing_artifact['file'],
        '-DpomFile=' + missing_artifact['pom']
    ]
    if 'sources' in missing_artifact:
        cmd.append('-Dsources=' + missing_artifact['sources'])
    if 'javadoc' in missing_artifact:
        cmd.append('-Djavadoc=' + missing_artifact['javadoc'])

    if verbose:
        print '[%s/%s] Command: %s' % (index + 1, len(missing_artifacts), ' '.join(cmd))
    else:
        print '\rDeploying %s of %s artifacts to remote repository...' % (index + 1, len(missing_artifacts)),

    if not dry_run:
        if verbose:
            subprocess.check_call(cmd)
        else:
            subprocess.check_output(cmd)

print '\rDeployed %s artifacts to remote repository...            ' % len(missing_artifacts)
print 'Done!'
