--step1
SELECT * FROM ET_Main.dbo.Members WHERE username = '%s'
--step1_end

--step2
SELECT KeyCode FROM [ET_Main].[dbo].[MemberSiteSetting] WHERE member_id = %d
--step2_end

--step3
DECLARE @studentID as int
Set @studentID ='%s'
DECLARE @starttime as datetime
Set @starttime='2015-09-05 06:54:38.433'

DECLARE @StudentLevelProgress_id as INT
DECLARE @StudentUnitProgress_id AS INT

SET @StudentLevelProgress_id =(SELECT StudentLevelProgress_id FROM SchoolAccount.dbo.StudentLevelProgress
WHERE StudentCourse_id in(
SELECT StudentCourse_id FROM SchoolAccount.dbo.StudentCourse
WHERE Student_id =@studentID 
AND IsCurrent=1 AND IsCurrentForCourseType=1 AND IsEnrollable=1 AND IsPrimary=1
)
)
SET @StudentUnitProgress_id=(SELECT MIN(StudentUnitProgress_id) FROM SchoolAccount.dbo.StudentUnitProgress
WHERE StudentCourse_id in (
SELECT StudentCourse_id FROM SchoolAccount.dbo.StudentCourse
WHERE Student_id =@studentID 
AND IsCurrent=1 AND IsCurrentForCourseType=1 AND IsEnrollable=1 AND IsPrimary=1
)
)

UPDATE SchoolAccount.dbo.StudentLevelProgress
SET StartDateTime=@starttime
WHERE StudentLevelProgress_id=@StudentLevelProgress_id

UPDATE SchoolAccount.dbo.StudentUnitProgress
SET StartDateTime=@starttime
WHERE StudentUnitProgress_id=@StudentUnitProgress_id
--step3_end

--step4
SELECT sci.id, sci.itemtype_id, sci.extradata, sci.score, * 
FROM school_0.dbo.StudentCourseItem sci 
WHERE sci.Student_id = %s
AND ItemType_id = 2
ORDER BY sci.ItemType_id, sci.id
--step4_end

--step5
UPDATE school_0.dbo.StudentCourseItem
set ExtraData = '%s'
where id = '%s'
and student_id = '%s'
--step5_end

--step6
SELECT * FROM oboe.dbo.ScheduledClass sc
WHERE sc.IsPublished = 1 AND sc.IsDeleted=0 AND sc.ClassCategory_id = %d
AND sc.StartDate BETWEEN '2016-07-01 01:00:00.000' AND GETDATE()
--step6_end

--step7

--F2F: 1, course: 3060099

--WS: 2, course: 3060100

--Apply(cool): 3, course: 3060101

--LC(mini): 6, course: 3060101
use oboe
declare @booking_id as int
declare @ScheduledClass_id as int
declare @student_id as int
declare @coupon_id as int
declare @couponClassCategoryGroup_id as int
declare @i as INT
declare @a bit
set @ScheduledClass_id = %d
set @student_id = %s
set @couponClassCategoryGroup_id = %d
set @i=1
SET @a = (SELECT COUNT(*) FROM dbo.Coupon where booking_id is NULL and student_id = @student_id 
and couponClassCategoryGroup_id=@couponClassCategoryGroup_id)
if (@a >= 1)
begin
 INSERT INTO Booking VALUES(@ScheduledClass_id,@student_id,'2',1,1,0,getdate()-3,getdate()-3,'1')
 select @booking_id=booking_id from Booking where student_id = @student_id and ScheduledClass_id=@ScheduledClass_id
 select @coupon_id = min(coupon_id) from dbo.Coupon where booking_id is NULL and student_id = @student_id 
  and couponClassCategoryGroup_id=@couponClassCategoryGroup_id AND IsActivated=1 AND IsDeleted=0
 update dbo.Coupon set booking_id = @booking_id where coupon_id=@coupon_id
end
else
    SELECT 'You have no enough coupon!!'
--step7_end
