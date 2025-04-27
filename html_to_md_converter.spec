# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['html_to_md_converter.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('/Users/lea/Desktop/venv-for-pyinstaller/lib/python3.11/site-packages/bs4', 'bs4')
    ],
    hiddenimports=['bs4', 'html.parser'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='html_to_md_converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='html_to_md_converter',
)
app = BUNDLE(
    coll,
    name='html_to_md_converter.app',
    icon=None,
    bundle_identifier=None,
)
