import ScriptingBridge

iTunes = ScriptingBridge.SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

print(iTunes.currentTrack().name())
