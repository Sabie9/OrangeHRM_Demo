cd C:\Users\Somparna\PycharmProjects\OrangeHRM_Demo

rem chrome-section
python -m pytest -v -s -m "sanity" --html=Reports\report-sanity-chrome.html testCases/ --browser chrome
rem python -m pytest -v -s -m "sanity or DDT" --html=Reports\report-sanity-DDT-chrome.html testCases/ --browser chrome
rem python -m pytest -v -s -m "regression and DDT" --html=Reports\report-regression-DDT-chrome.html testCases/ --browser chrome
rem python -m pytest -v -s -m "regression" --html=Reports\report-regression-chrome.html testCases/ --browser chrome

rem firefox-section
rem python -m pytest -v -s -m "sanity" --html=Reports\report-sanity-firefox.html testCases/ --browser chrome
rem python -m pytest -v -s -m "sanity or DDT" --html=Reports\report-sanity-DDT-firefox.html testCases/ --browser chrome
rem python -m pytest -v -s -m "regression and DDT" --html=Reports\report-regression-DDT-firefox.html testCases/ --browser chrome
rem python -m pytest -v -s -m "regression" --html=Reports\report-regression-firefox.html testCases/ --browser chrome

rem edge-section
rem python -m pytest -v -s -m "sanity" --html=Reports\report-sanity-edge.html testCases/ --browser chrome
rem python -m pytest -v -s -m "sanity or DDT" --html=Reports\report-sanity-DDT-edge.html testCases/ --browser chrome
rem python -m pytest -v -s -m "regression and DDT" --html=Reports\report-regression-DDT-edge.html testCases/ --browser chrome
rem python -m pytest -v -s -m "regression" --html=Reports\report-regression-edge.html testCases/ --browser chrome