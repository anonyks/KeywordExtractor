@echo off
echo made by @ANONYKS_XD

set "dir=%~dp0"
echo Directory: %dir%

echo Enter keyword to search:
set /p keyword="> "

echo =======================Start Sorting=============================================
for /r %dir% %%f in (*.txt) do (
  FINDSTR /L "%keyword%" "%%f" >> %keyword%.txt
)
echo =======================Combo Save========================================
echo =======================Sort Complete=============================================

pause

@del /q temp.txt
