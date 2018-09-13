--step0
select MemberId,PartnerSite from ET_Main.dbo.Members
where UserName = '%s'
--step0_end


--step1
update et_commerce..Subscriptions
set DateEntered= '{}', dateactivated = '{}'
where MemberId = {}
update et_commerce..featureAccessGrants
set activefrom  ='{}'
where memberid = {}
--step1_end

--step2
update oboe..StudyPlan
set StartDate = '{}'
where Student_id = {}
--step2_end


--step3
select * from school_{}..studentcourseitem
where student_id = {} and itemtype_id = 2 -- itemtype_id = 2 means level
--step3_end

--step4
update school_{}..studentcourseitem
set CompleteDate = '{}',
StartDate = '{}' ,
ExtraData = '{}'
where id = {} -- id from school_x..studentcourseitem
--step4_end

--step5
-- select offline class id，1=F2F, 2=WS, 3=Apply(Cool),4=LC(Mini)
SELECT * from oboe.dbo.ScheduledClass sc
INNER JOIN oboe.dbo.School_lkp sl
ON sc.School_id = sl.School_id
WHERE sc.ClassCategory_id = {}
AND sc.IsDeleted = 0
AND sc.IsPublished = 1
AND sl.PartnerCode = '{}'
and sc.StartDate BETWEEN '{}' AND '{}'
--step5_end

--step6
--Add offline class, need to update student_id , ScheduledClass_id,  couponClassCategoryGroup_id(1=F2F, 2=WS, 3=Apply(Cool), 4=LC(Mini)) ,  and the variable i(how many lessons)
use oboe
declare @booking_id as int
declare @ScheduledClass_id as int
declare @student_id as int
declare @coupon_id as int
declare @couponClassCategoryGroup_id as int
declare @i as INT
declare @a bit
set @ScheduledClass_id = {}
set @student_id = {}
set @couponClassCategoryGroup_id = {}
set @i=1
WHILE @i <= 1
Begin
SET @a = (SELECT COUNT(*) FROM dbo.Coupon where booking_id is NULL and student_id = @student_id
and couponClassCategoryGroup_id=@couponClassCategoryGroup_id)
if (@a >= 1)
begin
      INSERT INTO Booking VALUES(@ScheduledClass_id,@student_id,'2',4,1,0,getdate()-3,getdate()-3,'4','pc')
       select @booking_id=booking_id from Booking where student_id = @student_id and ScheduledClass_id=@ScheduledClass_id
       select @coupon_id = min(coupon_id) from dbo.Coupon where booking_id is NULL and student_id = @student_id
              and couponClassCategoryGroup_id=@couponClassCategoryGroup_id AND isdeleted=0
       update dbo.Coupon set booking_id = @booking_id where coupon_id=@coupon_id
end
else
    SELECT 'You have no enough coupon!!'
set @i = @i+1
End
--step6_end
