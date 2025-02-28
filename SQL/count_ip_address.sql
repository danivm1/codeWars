DECLARE @ip1 VARCHAR(20) = '10.0.1.10'
       ,@ip2 VARCHAR(20) = '10.0.2.0'


SELECT result = SUM(a.val)
FROM (SELECT val = (val2 * POWER(256, rn)) - (val1 * POWER(256, rn))
      FROM (SELECT x1.rn
                  ,x1.val1
                  ,x2.val2
            FROM (SELECT rn = 4 - ROW_NUMBER() OVER (ORDER BY (SELECT NULL))
                        ,val1 = CAST(VALUE AS INT)
                  FROM STRING_SPLIT(@ip1, '.')) AS x1
            INNER JOIN (SELECT rn = 4 - ROW_NUMBER() OVER (ORDER BY (SELECT NULL))
                              ,val2 = VALUE
                        FROM STRING_SPLIT(@ip2, '.')) AS x2
            ON x1.rn = x2.rn) AS x) AS a