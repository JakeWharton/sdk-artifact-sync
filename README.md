SDK Artifact Sync
=================

A Python script which synchronizes all of the artifacts in your local Android SDK to a remote Maven artifact host.

The Java development community has been distributing binary artifacts in a standard way since before Android existed.
Build tools, continuous integration software, and corporate infrastructure exists to handle this standard distribution
mechanism. Google, however, continues to ignore this standard distribution mechanism for their Android libraries despite
its use for their other open source projects and other official product libraries. Android developers are required to
use their bespoke SDK manager for downloading entire Maven repositories as one giant artifact on every machine.

This script unburdens you from this mechanism and instead synchronizes these artifacts to a remote artifact host of your
choice. This will allow your build tools to resolve and cache these artifacts automatically.


Usage
-----

Before using this script, be sure that you only distribute the artifacts within the SDK in accordance to the license
which you accepted when downloading them blah blah blah...

    usage: sdk-artifact-sync.py [-h] [--sdk SDK] [--dry-run] [-v] repo_id repo_url

    Synchronize SDK artifacts with a remote Maven repo

    positional arguments:
      repo_id        Remote repository ID (for authentication via settings.xml).
      repo_url       Remote repository URL.

    optional arguments:
      -h, --help     show this help message and exit
      --sdk SDK      Path to Android SDK. Defaults to ANDROID_HOME.
      --dry-run      Prepare sync but do not execute.
      -v, --verbose  Print verbose logging.

For example,

    $ ./sdk-artifact-sync.py example-nexus https://nexus.example.com/content/repositories/android-sdk/
    Loaded 1150 artifacts from your local SDK.
    1134 of 1150 artifacts missing from remote.
    Deploying 393 of 1134 artifacts to remote repository...

This script uses Maven to deploy each artifact. Ensure you have a modern version of Maven (`mvn`) installed. The
`repo_id` argument corresponds to an ID in your `~/.m2/settings.xml`. For example,

```xml
<settings>
  <servers>
    <server>
      <id>example-nexus</id>
      <username>jw</username>
      <password>hunter2</password>
    </server>
  </servers>
</settings>
```

Once all the artifacts are synchronized to your remote host you can remove the local SDK repositories from your builds:

```groovy
// Suppress local repos coming from the Android SDK. TODO switch to http://b.android.com/222372
repositories.all { repository ->
  if (repository instanceof MavenArtifactRepository) {
    MavenArtifactRepository r = (MavenArtifactRepository) repository;
    def url = r.url.toString()
    if (url.contains('extras/') && url.contains('m2repository/')) { // Good enough for now...
      println('Suppressing repository ' + url + ' in ' + project.name)
      repositories.remove(repository)
    }
  }
}
```

Please [star this issue](http://b.android.com/222372) to make this operation easier in the future.



License
=======

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
