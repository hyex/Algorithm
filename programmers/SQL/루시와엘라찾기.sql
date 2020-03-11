-- v1 내 코드

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE 
FROM ANIMAL_INS
WHERE NAME = 'Lucy' OR NAME = 'Ella' OR NAME = 'Pickle' OR NAME = 'Rogan' OR NAME = 'Sabrina' OR NAME = 'Mitty'
ORDER BY ANIMAL_ID

-- v2 더 좋은 방안

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
