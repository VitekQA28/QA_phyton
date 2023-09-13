@echo off

set results=./allure-files
set rep_history=./allure-report/history
set report=./allure-report

rmdir /s /q %results%
pytest --alluredir=%results%
move %rep_history% %results%
rmdir /s /q %report%
allure generate %results% -o %report%
allure open %report%