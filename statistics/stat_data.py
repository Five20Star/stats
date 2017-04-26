#coding:utf-8
from statistics.data_source import DataSource
from datetime import datetime,timedelta


class StatData(object):
    
    def __init__(self,dir_path):
        self.dt=DataSource(dir_path)
    def get_seconds(self,strings):
        slist=strings.split(':')
        return 3600*int(slist[0])+60*int(slist[1])+int(slist[2])

    def show(self):
        print self.dt.tianrong_rs
        print self.dt.qingniu_rs
        print self.dt.gude_rs

    def load_tianrong_data(self):
        tr_list=self.dt.tianrong_rs
        rs_map={}
        for it in tr_list:
            wid = it.worker_id
            if wid not in rs_map:
                rs_map[wid]={}
            date=datetime.strptime(it.start_time,'%Y-%m-%d %H:%M:%S')
            inner_key = str(date.date())
            if inner_key not in rs_map[wid]:
                rs_map[wid][inner_key]={'date':None,
                    'name':None,
                    'worker_id':None,
                    'answer':0,
                    'unAnswer':0,
                    'call_times':0,
                    'call_duration':0.0,
                    'avg_call_duration':0.0,
                    'valid_call_times':0,
                    'valid_call_duration':0,
                    'valid_call_avg_duration':0,
                    'valid_call_radio':'',
                }
            rs_map[wid][inner_key]['date'] = date
            rs_map[wid][inner_key]['name'] = it.worker_name
            rs_map[wid][inner_key]['worker_id'] = it.worker_id
            rs_map[wid][inner_key]['answer'] += 1 if it.call_stat==u'人工接听' else 0 #人工接听
            rs_map[wid][inner_key]['unAnswer'] += 0 if it.call_stat==u'人工接听' else 1   #人工未接听
            rs_map[wid][inner_key]['call_times'] = rs_map[wid][inner_key]['answer']+rs_map[wid][inner_key]['unAnswer'] #来电数
            rs_map[wid][inner_key]['call_duration'] += it.call_duration.second   #通话总时长
            rs_map[wid][inner_key]['avg_call_duration'] = rs_map[wid][inner_key]['call_duration']/(rs_map[wid][inner_key]['answer'] or 1)   #平均通话时长
            rs_map[wid][inner_key]['valid_call_times'] += 1 if it.call_duration.second>=15*60 else 0 #有效通话次数
            rs_map[wid][inner_key]['valid_call_duration'] += it.call_duration.second if it.call_duration.second>=15*60 else 0  #有效通话时长
            rs_map[wid][inner_key]['valid_call_avg_duration'] = rs_map[wid][inner_key]['valid_call_duration']/(rs_map[wid][inner_key]['valid_call_times'] or 1) #有效通话平均时长
            rs_map[wid][inner_key]['valid_call_radio'] = rs_map[wid][inner_key]['valid_call_times']/(rs_map[wid][inner_key]['answer'] or 1)  #有效通话率
        return rs_map
    def load_gude_data(self):
        gd_list = self.dt.gude_rs
        rs_map={}
        for it in gd_list:
            wid = it.worker_id
            if wid not in rs_map:
                rs_map[wid]={}
            rs_map[wid]['gd_call_duration']= self.get_seconds(it.call_duration) #通话总时长
            rs_map[wid]['gd_call_times'] = int(it.connection_nums)       #通话次数
            rs_map[wid]['gd_call_in_ctimes'] = int(it.total_connection)    #接通次数
            rs_map[wid]['gd_call_avg_duration'] = rs_map[wid]['gd_call_duration']/(rs_map[wid]['gd_call_in_ctimes'] or 1) #平均通话时长
            rs_map[wid]['gd_valid_call_nums'] = int(it.call_out_invalid_nums) #有效通话次数
            rs_map[wid]['gd_valid_call_duration'] = it.call_in_connect_duraion  #有效通话时长
            rs_map[wid]['gd_valid_call_avg_duration'] = it.call_out_connect_avg_duraion    #有效通话平均时长
            rs_map[wid]['gd_valid_call_radio'] = rs_map[wid]['gd_valid_call_nums']/(rs_map[wid]['gd_call_in_ctimes'] or 1) #有效通话率
        return rs_map
    def load_qingniu_data(self):
        qn_list = self.dt.qingniu_rs
        rs_map={}
        for it in qn_list:
            wid = len(str(it.worker_id))==2 and '00'+str(it.worker_id) or str(it.worker_id)
            if wid not in rs_map:
                rs_map[wid]={}
            date=datetime.strptime(it.start_time.replace(u'下午 ','').replace(u'上午 ',''),'%Y-%m-%d %H:%M:%S')
            inner_key = str(date.date())
            if inner_key not in rs_map[wid]:
                rs_map[wid][inner_key]={
                    'qn_name':None,
                    'qn_woker_id':None,
                    'qn_worker_no':None,
                    'qn_call_duration':0,
                    'qn_call_times':0,
                    'qn_valid_call_times':0,
                    'qn_valid_call_all_duration':0,
                    'qn_valid_avg_call_duration':0,
                    'qn_valid_call_radio':0
                }
            rs_map[wid][inner_key]['qn_call_duration']+=self.get_seconds(it.all_duration)   #通话总时长
            rs_map[wid][inner_key]['qn_call_times']+=1 #通话总次数
            rs_map[wid][inner_key]['qn_avg_call_duration'] = rs_map[wid][inner_key]['qn_call_duration']/(rs_map[wid][inner_key]['qn_call_times'] or 1)   #平均通话时长
            rs_map[wid][inner_key]['qn_valid_call_times'] = 1 if self.get_seconds(it.call_duration)>180 else 0  #有效通话次数
            rs_map[wid][inner_key]['qn_valid_call_all_duration'] =  self.get_seconds(it.call_duration) if self.get_seconds(it.call_duration)>180 else 0   #有效通话时长
            rs_map[wid][inner_key]['qn_valid_avg_call_duration'] =  rs_map[wid][inner_key]['qn_valid_call_all_duration']/(rs_map[wid][inner_key]['qn_valid_call_times'] or 1)  #有效通话平均时长 
            rs_map[wid][inner_key]['qn_valid_call_radio'] =  rs_map[wid][inner_key]['qn_valid_call_times']/(rs_map[wid][inner_key]['qn_call_times'] or 1)  #有效通话率

        return rs_map

    def get_tr_rs(self):
        rs=self.load_tianrong_data()
        rs_gude=self.load_gude_data()
        rs_qn=self.load_qingniu_data()
        print rs_qn.keys()
        print rs.keys()
        rs_gude_default={
            'gd_call_duration':'---',
            'gd_call_times':'---',
            'gd_call_in_ctimes':'---',
            'gd_call_avg_duration':'---',
            'gd_valid_call_nums':'---',
            'gd_valid_call_duration':'---',
            'gd_valid_call_avg_duration':'---',
            'gd_valid_call_radio':'---'
        }
        rs_qn_default={
            'qn_name':'---',
            'qn_woker_id':'---',
            'qn_worker_no':'---',
            'qn_call_duration':'---',
            'qn_call_times':'---',
            'qn_valid_call_times':'---',
            'qn_valid_call_all_duration':'---',
            'qn_valid_avg_call_duration':'---',
            'qn_valid_call_radio':'---'
        }
        rs_map={}
        for k,v in rs.items():
            for kk,vv in v.items():
                if kk not in rs_map:
                    rs_map[kk]=[]
                gu_item = k in rs_gude and rs_gude[k] or rs_gude_default
                vv.update(gu_item)
                if k in rs_qn and kk in rs_qn[k]:
                    vv.update(rs_qn[k][kk])
                else:
                    vv.update(rs_qn_default)
                rs_map[kk].append(vv)

        return sorted(rs_map.items())


if __name__=='__main__':
    pass