-- MySQL

/*
* DOCTOR 테이블에서,
* MCDP_CD가 흉부외과(CS) 이거나 일반외과(GS)인
* 의사의 이름(DR_NAME), 의사 ID(DR_ID), 진료과(MCDP_CD), 고용일자(HIRE_YMD) 를 조회
* 단, 고용일자를 기준으로 내림차순, 이름을 기준으로 오름차순
*/

-- HIRE_YMD를 그냥 출력하면, 시간까지 나와서 정답이 되지 않음.
-- DATE_FORMAT(, '%Y-%m-%d')를 사용하여 포맷을 맞춰줌.

SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD IN ('CS', 'GS')
ORDER BY HIRE_YMD DESC, DR_NAME ASC;