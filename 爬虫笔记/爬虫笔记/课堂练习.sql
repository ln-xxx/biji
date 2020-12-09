--  查询名字性别
 SELECT name,sex FROM tbl_student

--  查询所有老师
 SELECT * FROM tbl_teacher WHERE sex = '女' AND age>=28

--  查询男生
 SELECT * FROM tbl_student WHERE sex = '男'

--  查询年龄小于30，性别为男条件
 SELECT * FROM tbl_student WHERE sex = '男' AND age<30 

--  查询年龄小于30，性别为男条件
 SELECT * FROM tbl_student WHERE sex = '男' OR age<20

--  模糊查询名字中带有张的
 SELECT * FROM tbl_teacher WHERE name LIKE '%张%'
--  模糊查询名字带有张的’_‘表示单一的
 SELECT * FROM tbl_teacher WHERE name LIKE '张_'

--  模糊查询名字中带有张的名字"%"表示多个字符
 SELECT * FROM tbl_teacher WHERE name LIKE '张%'
 SELECT * FROM tbl_teacher WHERE name LIKE '张__'

-- 年龄排序order BY/asc升序/desc降序
 SELECT * FROM tbl_student ORDER BY age ASC
 SELECT * FROM tbl_student ORDER BY age DESC

-- 分页/限制 前三条信息
 SELECT * FROM tbl_teacher LIMIT 5
-- 每页三条查第二页（开始=(页数-1)*页数)，显示条数=（页数*每页数）
 SELECT * FROM tbl_student LIMIT 4,6
 SELECT * FROM tbl_score LIMIT 5,3
-- 查所有男生（每页三条），第二页,年龄排序
 SELECT * FROM tbl_student WHERE sex = '男' 
 ORDER BY age ASC 
 LIMIT 3,3
-- 查询总条数
SELECT count(*) FROM tbl_student WHERE sex = '男' 
SELECT count(*) as '女生总数' FROM tbl_student 

-- 查询最大年龄，最小年龄，平均年龄
SELECT max(age) as '最大年龄' FROM tbl_teacher
SELECT min(age) as '最小年龄' FROM tbl_teacher
SELECT avg(age) as '平均年龄' FROM tbl_teacher

--增加数据
 INSERT INTO tbl_student VALUES(11,'赵11','男',20,'19980105','湖南');
 INSERT INTO tbl_student(name,sex,age) VALUES('习大大','男',60);

-- 修改性别 
UPDATE tbl_student SET sex = '女' WHERE name = '姚宏伟'

-- 设置id>5的所有的班级为“1班”
SELECT * FROM tbl_class WHERE name = '1班'
UPDATE tbl_student SET cid = 1 WHERE id>5

-- 删除年龄为空的信息

SELECT * FROM tbl_student WHERE age = ''
SELECT * FROM tbl_student WHERE age IS NULL
UPDATE tbl_student SET address = '' WHERE id=12

DELETE FROM tbl_student WHERE id=12

INSERT INTO tbl_student(name,sex,age,birthday,address) VALUES('习大大','男',60,'18891010','陕西')

SELECT stu.name,stu.sex FROM tbl_student as stu



-- 多表联查
SELECT stu.name , c.name 
FROM tbl_student as stu,tbl_class as c
WHERE stu.cid = c.id


-- join on 
SELECT s.name ,g.name
FROM tbl_student as s JOIN tbl_class as g 
ON s.cid = g.id 

SELECT s.id,s.name,s.sex
FROM tbl_teacher as s


-- -- -- --查学生名，课程名，分数
SELECT s.id,stu.name,c.name,s.score
FROM tbl_student stu,tbl_timetable c,tbl_score s
WHERE s.stu_id = stu.id AND s.time_id = c.id

-- -- -- 查询人数
SELECT cid,count(*) as renshu
FROM tbl_student GROUP BY cid
-- --分组后加条件
HAVING renshu>2 
