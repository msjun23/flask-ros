import pymysql
 
class xsens_db:
    def __init__(self):
        pass
    
    def GetGPS(self):
        ret = []
        db = pymysql.connect(host='localhost', user='aril', db='xsens_db', password='1234', charset='utf8')
        curs = db.cursor()
        
        sql = "SELECT * FROM gps_data ORDER BY seq DESC LIMIT 1";
        curs.execute(sql)
        
        rows = curs.fetchall()
        for data in rows:
            # seq
            # time_stamp
            # latitude
            # longitude
            # altitude
            temp = {'seq':data[0], 'time_stamp':data[1], 'latitude':data[2],'longitude':data[3],'altitude':data[4] }
            ret.append(temp)
        
        db.commit()
        db.close()
        return ret
    
    def GetIMU(self):
        ret = []
        db = pymysql.connect(host='localhost', user='aril', db='xsens_db', password='1234', charset='utf8')
        curs = db.cursor()
        
        sql = "SELECT * FROM imu_data ORDER BY seq DESC LIMIT 1";
        curs.execute(sql)
        
        rows = curs.fetchall()
        for data in rows:
            # seq
            # time_stamp
            # quaternion_w
            # quaternion_x
            # quaternion_y
            # quaternion_z
            # linear_acceleration_x
            # linear_acceleration_y
            # linear_acceleration_z
            # angular_velocity_x
            # angular_velocity_y
            # angular_velocity_z
            temp = {'seq':data[0], 'time_stamp':data[1], \
                    'quaternion_w':data[2],'quaternion_x':data[3],'quaternion_y':data[4],'quaternion_z':data[5], \
                    'linear_acceleration_x':data[6], 'linear_acceleration_y':data[7], 'linear_acceleration_z':data[8], \
                    'angular_velocity_x':data[9], 'angular_velocity_y':data[10], 'angular_velocity_z':data[11]}
            ret.append(temp)
        
        db.commit()
        db.close()
        return ret
    
    def delEmp(self, empno):
        db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
        curs = db.cursor()
        
        sql = "delete from emp where empno=%s"
        curs.execute(sql,empno)
        db.commit()
        db.close()
 
if __name__ == '__main__':
    #MyEmpDao().delEmp('aaa')
    gps_list = xsens_db().GetGPS();
    imu_list = xsens_db().GetIMU();
    print(gps_list)
    print(imu_list)
    