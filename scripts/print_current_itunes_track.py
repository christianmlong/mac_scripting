"""

    print_current_itunes_track.py

    Quick demo of the Python-ObjectiveC bridge.

    pip install pyobjc

    https://pythonhosted.org/pyobjc/

"""

import ScriptingBridge

iTunes = ScriptingBridge.SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

print(iTunes.currentTrack().name())
