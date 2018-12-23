# -*- mode: python -*-

block_cipher = None


a = Analysis(['label_tool.py'],
             pathex=['Digitize.py', 'ImgLabel.py', 'rcs_rc.py', 'test.py', 'tools.py', 'C:\\Users\\chen\\Anaconda3\\envs\\python35\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\chen\\Desktop\\cepha_landmark_label_gui'],
             binaries=[],
             datas=[],
             hiddenimports=['test', 'ImgLabel', 'tools'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='label_tool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='logo.ico')
