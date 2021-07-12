# Capstoneproject
It is a travel diary, where a viewer can store their travel information in the diary.
Venue: The city details are added
Place: The places inside the city is added.

Steps to proceed:

pip install virtualenv    

virtualenv venv   

source venv/bin/activate

pip install -r requirements.txt

flask db migrate  

flask db upgrade

pip install psychopg2-binary

FLASK_APP=app.py FLASK_DEBUG=TRUE flask run

Create Account in auth0 and give permissions.

Run test_run.py for test cases running

Deploy using heorku


Roles:
Admin: The creater will have all permissions for both venue and places
Bearer token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllRT2dPZ3F0djRHaS1tTkVqd29LayJ9.eyJpc3MiOiJodHRwczovL2tpdHR1LWZzbmQudXMuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAyODczNDM1NDAzMzA4Njg1MjM1IiwiYXVkIjoidHJhdmVsIiwiaWF0IjoxNjI2MDcxMjMyLCJleHAiOjE2MjYwNzg0MzIsImF6cCI6IlZkcUhsVmU5STR2UGxMWmlqTlpQNnVOVndCSnBaR2U1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cGxhY2UiLCJkZWxldGU6dmVudWUiLCJnZXQ6cGxhY2VzIiwiZ2V0OnZlbnVlcyIsInBhdGNoOnBsYWNlcyIsInBhdGNoOnZlbnVlcyIsInBvc3Q6cGxhY2UiLCJwb3N0OnZlbnVlIl19.JcMbOwF1bA4BIDadE2hyoXR-6klq1OpECYlBH-sdSK3Epn55xXGiEZA2b2XHE67_CNB_FSD2i--UPbpqhrbPCsV2NHP1ILk5KKcYO6JFbvE91sZjSjwG5e2sqNlrv8wZSansRPnTYHRmvco0Qh9KVOLxvW0aa2J_VCrKjxdTL4eVU7vs7QJhBBiPwuJvHJ36mnFWSjcQiIk5UufDe2KH8j3gskiX9TTh2WhOu0SlTm8r1dw9oKtHmlAgbAqsn3HBNXgm6xfB5du6fs762cVvPdrxeLERy_J-_MEdyXPbFlQP42Me-_8ROp9tuG2SvBh5kvkq-tZMFxhI2iY48I1kqw


Co-Admin: The co traveller will have all rights except update or deleting the venue.
Bearer token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRqSVlBRkVRdFphVkJKTENWTC1rbCJ9.eyJpc3MiOiJodHRwczovL2tpdHR1Mi1mc25kLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjkxMjg1NjkwNTIyNDU2MDM5MCIsImF1ZCI6InRyYXZlbCIsImlhdCI6MTYyNjA3NDE3MCwiZXhwIjoxNjI2MDgxMzcwLCJhenAiOiJJczUwOTd4N0dPbDh4Q1R6S0V3NzRxWXFtU2tjbWYxaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnBsYWNlIiwiZ2V0OnBsYWNlcyIsImdldDp2ZW51ZXMiLCJwYXRjaDpwbGFjZXMiLCJwYXRjaDp2ZW51ZXMiLCJwb3N0OnBsYWNlIl19.R0qHRM6If9wqIzeyasLLSs84jeZmZN2jW3hHe-xvpcY90PEo2DMvWm_WjSYyJs6KyBXw_dLFMNjNfG--jA44Ne3kuZjCIBNuBqHFrIVVrcwzIXbH54VR3KeP9yi-Uxd7T0O0YO49Vs--Kq6oSvV_pZIeouoSMu_PXxURw2Lnv5omNhrJjVNMwqRGiSttKMJfx1fe7eg1KUsV4cKY-5CIEn7TwBJyBNLmjZK5DLXIJ5pU9lqkOQYdg-p7hXS18fUDR-nJN-h6w2mZThP88HPwIdUBHwrNdYMSIXEg3srUEi1RO1Xz1jIcCIEkF6QEG81GasBuQIqFIObJ7T-nTskjPg

Viewer: They can only view the places and venues.

Bearer Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlQ4Ymt4SkQ3ZFpDMDFpX0xud1c3YyJ9.eyJpc3MiOiJodHRwczovL2tpdHR1My1mc25kLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMjc2NjE5NTA0MjkyNjU2MjAyMiIsImF1ZCI6InRyYXZlbCIsImlhdCI6MTYyNjA3NDgxNywiZXhwIjoxNjI2MDgyMDE3LCJhenAiOiJ6emEzb1ZFS0s2eXhPSU1Rb3hJMjhzbWViZDFJQUdtZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOltdfQ.O8eD3hNKKMvuho4v35UK1PNBhMa2gF53gQnTdUPxyte1qlhaeE1q4uY90lTcKW1G0QIN8ZvR4Iee-F98vBOf5HLGRpOL3N2PGNN5Ozrpr4WK-J_oO58ZTqqoa_m01bncljXa8HP1nHukq28muJOnG2D5wlkdXOdbeF3GlKYf6X3rfq32-0WJ00l3XdhQECVs0YKIyQ8Ui9I40tTnNW9P5LNc8uK7ztz0Zugu5ZiOmwqCwE-jDNZwCHfjFhyrSIsx1hTPSe5fYXZqdjWr7EYUDIP1cL2vHrFPRPtL8Av3W0lONn3Q3Jw-1Fga3A-yT_dG2rg9Wh46oKATWNp4edXisQ

Deployed using heroku at the below link:
https://git.heroku.com/travelldiar.git



