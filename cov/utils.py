import pymysql


def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="root",
                           db="cov",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def get_confirmed_data():
    sql = """
    SELECT total,total-heal-dead,heal,dead from (
    select sum(confirm) total, 
    (SELECT heal from history ORDER BY ds desc LIMIT 1) heal ,
      sum(dead) dead 
    from details where update_time=(
      select update_time from details order by update_time desc limit 1)
    ) d;
    """
    res = query(sql)
    return list(res[0])


def get_wordcloud_data():
    """
    :return:  返回热搜数据
    """
    sql = 'select content from hotsearch order by id desc limit 30'
    res = query(sql)  # 格式 (('民警抗疫一线奋战16天牺牲 1037364',), ('四川再派两批医疗队 1537382',)
    return res


def get_region_list():
    """
    :return:  返回各省份的剩余确诊人数
    """
    sql = 'SELECT update_time,province,city,confirm,confirm_add,confirm_now,heal,dead FROM details'
    res = query(sql)
    res = list(res)
    # print(res)
    # print(type(res))
    return res


def get_his_list():
    """
    :return:  返回疫情历史数据
    """
    sql = 'SELECT ds,confirm,confirm_now,suspect,heal,heal_add,dead,dead_add FROM history'
    res = query(sql)
    res = list(res)
    # print(res)
    # print(type(res))
    return res


def get_area_data():
    """
    :return:  返回疫情最新各地疫情数据
    """
    sql = "select end_update_time,province,city,county,address,type" \
          " from risk_area " \
          "where end_update_time=(select end_update_time " \
          "from risk_area " \
          "order by end_update_time desc limit 1) "
    res = query(sql)
    return list(res)


def get_echarts_data():
    """
    :return:  返回现有确诊人数前10名的省份
    """
    sql = 'SELECT province,confirm FROM ' \
          '(select province ,sum(confirm_now) as confirm from details  ' \
          'where update_time=(select update_time from details ' \
          'order by update_time desc limit 1) ' \
          'group by province) as a ' \
          'ORDER BY confirm DESC LIMIT 10'
    res = query(sql)
    return res