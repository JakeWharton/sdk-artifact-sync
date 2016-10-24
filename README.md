SDK Artifact Sync
=================

A Python script which synchronizes all of the artifacts in your local Android SDK to a remote Maven artifact host.

The Java development community has been distributing binary artifacts in a standard way since before Android existed.
Build tools, continuous integration software, and corporate infrastructure exists to handle this standard distribution
mechanism. Google, however, continues to ignore this standard distribution mechanism for their Android libraries despite
its use for their other open source projects and other official product libraries. Android developers are required to
use their bespoke SDK manager for downloading entire Maven repositories as one giant artifact on every machine.

This script unburdens you from their mechanism and instead synchronizes these artifacts to a remote artifact host of your
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
    Loaded 1204 artifacts from your local SDK.
    Checking for 1204 artifacts on remote...............................................................................
    ....................................................................................................................
    ....................................................................................................................
    ....................................................................✗..✗............................................
    ........✗......................✗....................................................................................
    ..................✗....................✗....................................................✗.......................
    ..............✗.....✗.................................✗.............✗........✗......................✗✗..............
    .............✗.............✗✗...✗.✗.✗....................✗..............................✗✗..✗.........✗✗............
    ...✗.................✗..........✗.✗.................✗..✗.............✗.......✗......✗........✗........✗.........✗...
    ............✗............✗..........✗............✗.......✗..........................✗...✗........✗....✗............✗
    .......✗..✗....................✗.........✗.......................✗.......✗..........
    54 of 1204 artifacts missing from remote.
    [1 / 54] Deploying com.google.android.gms:play-services:9.6.1... Done!
    [2 / 54] Deploying com.google.android.gms:play-services-ads:9.6.1... Done!
    [3 / 54] Deploying com.google.android.gms:play-services-ads-lite:9.6.1... Done!
    [4 / 54] Deploying com.google.android.gms:play-services-all-wear:9.6.1... Done!
    [5 / 54] Deploying com.google.android.gms:play-services-analytics:9.6.1... Done!
    [6 / 54] Deploying com.google.android.gms:play-services-analytics-impl:9.6.1... Done!
    [7 / 54] Deploying com.google.android.gms:play-services-appindexing:9.6.1... Done!
    [8 / 54] Deploying com.google.android.gms:play-services-appinvite:9.6.1... Done!
    [9 / 54] Deploying com.google.android.gms:play-services-auth:9.6.1... Done!
    [10 / 54] Deploying com.google.android.gms:play-services-auth-base:9.6.1... Done!
    [11 / 54] Deploying com.google.android.gms:play-services-awareness:9.6.1... Done!
    [12 / 54] Deploying com.google.android.gms:play-services-base:9.6.1... Done!
    [13 / 54] Deploying com.google.android.gms:play-services-basement:9.6.1... Done!
    [14 / 54] Deploying com.google.android.gms:play-services-cast:9.6.1... Done!
    [15 / 54] Deploying com.google.android.gms:play-services-cast-framework:9.6.1... Done!
    [16 / 54] Deploying com.google.android.gms:play-services-clearcut:9.6.1... Done!
    [17 / 54] Deploying com.google.android.gms:play-services-drive:9.6.1... Done!
    [18 / 54] Deploying com.google.android.gms:play-services-fitness:9.6.1... Done!
    [19 / 54] Deploying com.google.android.gms:play-services-games:9.6.1... Done!
    [20 / 54] Deploying com.google.android.gms:play-services-gass:9.6.1... Done!
    [21 / 54] Deploying com.google.android.gms:play-services-gcm:9.6.1... Done!
    [22 / 54] Deploying com.google.android.gms:play-services-identity:9.6.1... Done!
    [23 / 54] Deploying com.google.android.gms:play-services-iid:9.6.1... Done!
    [24 / 54] Deploying com.google.android.gms:play-services-instantapps:9.6.1... Done!
    [25 / 54] Deploying com.google.android.gms:play-services-location:9.6.1... Done!
    [26 / 54] Deploying com.google.android.gms:play-services-maps:9.6.1... Done!
    [27 / 54] Deploying com.google.android.gms:play-services-nearby:9.6.1... Done!
    [28 / 54] Deploying com.google.android.gms:play-services-panorama:9.6.1... Done!
    [29 / 54] Deploying com.google.android.gms:play-services-places:9.6.1... Done!
    [30 / 54] Deploying com.google.android.gms:play-services-plus:9.6.1... Done!
    [31 / 54] Deploying com.google.android.gms:play-services-safetynet:9.6.1... Done!
    [32 / 54] Deploying com.google.android.gms:play-services-tagmanager:9.6.1... Done!
    [33 / 54] Deploying com.google.android.gms:play-services-tagmanager-api:9.6.1... Done!
    [34 / 54] Deploying com.google.android.gms:play-services-tasks:9.6.1... Done!
    [35 / 54] Deploying com.google.android.gms:play-services-vision:9.6.1... Done!
    [36 / 54] Deploying com.google.android.gms:play-services-wallet:9.6.1... Done!
    [37 / 54] Deploying com.google.android.gms:play-services-wearable:9.6.1... Done!
    [38 / 54] Deploying com.google.firebase:firebase-ads:9.6.1... Done!
    [39 / 54] Deploying com.google.firebase:firebase-analytics:9.6.1... Done!
    [40 / 54] Deploying com.google.firebase:firebase-analytics-impl:9.6.1... Done!
    [41 / 54] Deploying com.google.firebase:firebase-auth:9.6.1... Done!
    [42 / 54] Deploying com.google.firebase:firebase-auth-common:9.6.1... Done!
    [43 / 54] Deploying com.google.firebase:firebase-auth-module:9.6.1... Done!
    [44 / 54] Deploying com.google.firebase:firebase-common:9.6.1... Done!
    [45 / 54] Deploying com.google.firebase:firebase-config:9.6.1... Done!
    [46 / 54] Deploying com.google.firebase:firebase-core:9.6.1... Done!
    [47 / 54] Deploying com.google.firebase:firebase-crash:9.6.1... Done!
    [48 / 54] Deploying com.google.firebase:firebase-database:9.6.1... Done!
    [49 / 54] Deploying com.google.firebase:firebase-database-connection:9.6.1... Done!
    [50 / 54] Deploying com.google.firebase:firebase-iid:9.6.1... Done!
    [51 / 54] Deploying com.google.firebase:firebase-invites:9.6.1... Done!
    [52 / 54] Deploying com.google.firebase:firebase-messaging:9.6.1... Done!
    [53 / 54] Deploying com.google.firebase:firebase-storage:9.6.1... Done!
    [54 / 54] Deploying com.google.firebase:firebase-storage-common:9.6.1... Done!
    Deployed 54 artifacts.

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
