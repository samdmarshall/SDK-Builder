import os
import subprocess
import shutil
import time
import sys
import argparse
import plistlib
from subprocess import CalledProcessError

# Globals
kVerboseLogLevel = 0;
kInstallPlatform = '';
kPlatformsPath = '';
# Helper Functions
def v_log(message, level, kVerboseLogLevel):
    if kVerboseLogLevel >= level:
        print message;
def should_update(installed, update):
    existing = os.path.getmtime(installed)
    updated = os.path.getmtime(update)
    return existing < updated
def make_dir(path):
    if file_exists(path) == False:
        os.mkdir(path)
def make_sym(original, path):
    if file_exists(path) == False:
        os.symlink(original, path)
def file_exists(path):
    return os.path.exists(path)
def make_xcrun_call(call_args):
    error = 0
    output = ''
    try:
        output = subprocess.check_output(call_args)
        error = 0
    except CalledProcessError as e:
        output = e.output
        error = e.returncode
    
    return (output, error)
def resolve_platform_path():
    platform_path = '';
    xcrun_result = make_xcrun_call(('xcrun', '--show-sdk-platform-path'));
    if xcrun_result[1] != 0:
        v_log('Please run Xcode first!',0, kVerboseLogLevel);
        sys.exit();
    
    platform_path = xcrun_result[0].rstrip('\n');
    platform_path = os.path.dirname(platform_path);
    return platform_path;
# Main
def main(argv):
    parser = argparse.ArgumentParser();
    parser.add_argument('-p','--platform', help='path to platform folder to install', required=True, action='store');
    parser.add_argument('-u','--update', help='update platform folder', action='store_true');
    parser.add_argument('-f','--force', help='force action', action='store_true');
    parser.add_argument('-v','--verbose', help='add verbosity', action='count');
    args = parser.parse_args();
    
    if args.verbose == None:
        kVerboseLogLevel = 0;
    else:
        kVerboseLogLevel = args.verbose;
    
    platform_name = os.path.basename(args.platform);
    kPlatformsPath = resolve_platform_path();
    platform_exists = platform_name in os.listdir(kPlatformsPath);
    kInstallPlatform = os.path.join(kPlatformsPath, platform_name);
    
    if platform_exists == True and args.force == True:
        v_log('Removing previous install of \''+platform_name+'\'. This will take a few minutes',0,kVerboseLogLevel);
        shutil.rmtree(kInstallPlatform);
        platform_exists = False;
    
    if platform_exists == False:
        v_log('Installing Platform...',0, kVerboseLogLevel);
        shutil.copytree(args.platform, kInstallPlatform);


if __name__ == "__main__":
    main(sys.argv[1:]);