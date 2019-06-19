from influxdb import InfluxDBClient

client = InfluxDBClient('192.168.29.154', 8086, 'root', 'root', 'steplog')

def ztest():
    sql='DROP CONTINUOUS QUERY "day4g" ON "steplog"'
    result=client.query(sql)
    print("Result: {0}".format(result))

def zcreate():
    sql='CREATE CONTINUOUS QUERY "wansMin" ON "steplog" BEGIN SELECT round(mean("rtt")) as rtt,round(mean("miss")) as miss , round(mean("rx")) as rx ,round(mean("tx")) as tx,round(mean("get")) as get,round(mean("post")) as post,round(mean("period")) as period INTO "1mth"."wans1mth" FROM "1w"."wans" GROUP BY time(20m),sn,iface,type END'
    client.query(sql)
    sql='CREATE CONTINUOUS QUERY "wansHour" ON "steplog" BEGIN SELECT round(mean("rtt")) as rtt,round(mean("miss")) as miss , round(mean("rx")) as rx ,round(mean("tx")) as tx,round(mean("get")) as get,round(mean("post")) as post,round(mean("period")) as period INTO "1y"."wans1y" FROM "1mth"."wans1mth" GROUP BY time(4h),sn,iface,type END'
    client.query(sql)
    sql='CREATE CONTINUOUS QUERY "pathtpMin" ON "steplog" BEGIN SELECT round(mean("rx")) as rx ,round(mean("tx")) as tx INTO "1mth"."pathtp1mth" FROM "1w"."pathtp" GROUP BY time(20m),tid,tp END'
    client.query(sql)
    sql='CREATE CONTINUOUS QUERY "pathtpHour" ON "steplog" BEGIN SELECT round(mean("rx")) as rx ,round(mean("tx")) as tx INTO "1y"."pathtp1y" FROM "1mth"."pathtp1mth" GROUP BY time(4h),tid,tp END'
    client.query(sql)
    sql='CREATE CONTINUOUS QUERY "tunnelgetMin" ON "steplog" BEGIN SELECT round(mean("get")) as get INTO "1mth"."tunnelget1mth" from "1w"."tunnelget" GROUP BY time(20m),tid END'
    client.query(sql)
    sql='CREATE CONTINUOUS QUERY "tunnelgetHour" ON "steplog" BEGIN SELECT round(mean("get")) as get INTO "1y"."tunnelget1y" from "1mth"."tunnelget1mth" GROUP BY time(4h),tid END'
    client.query(sql)
    sql='CREATE CONTINUOUS QUERY "tunnelMin" ON "steplog" BEGIN SELECT round(mean("rxrate")) as rxrate ,round(mean("txrate")) as txrate,round(mean("recv")) as recv,round(mean("send")) as send,round(mean("ct")) as ct,round(mean("load")) as load INTO "1mth"."tunnel1mth" FROM "1w"."tunnelinfo" GROUP BY time(20m),tid END'
    client.query(sql)
    sql='CREATE CONTINUOUS QUERY "tunnelHour" ON "steplog" BEGIN SELECT round(mean("rxrate")) as rxrate ,round(mean("txrate")) as txrate,round(mean("recv")) as recv,round(mean("send")) as send,round(mean("ct")) as ct,round(mean("load")) as load INTO "1y"."tunnelinfo1y" FROM "1mth"."tunnelinfo1mth" GROUP BY time(4h),tid END'
    result=client.query(sql)
    print("Result: {0}".format(result))
    sql='SELECT * INTO "1w"."wans" FROM "1w"."wans1w" GROUP BY *'
    client.query(sql)
    sql='SELECT * INTO "1mth"."tunnelinfo1mth" FROM "1mth"."tunnel1mth" GROUP BY *'
    client.query(sql)

def dclear():
    client.drop_measurement('wans1w')
    client.drop_measurement('tunnel1mth')
    sql='DROP CONTINUOUS QUERY "tunnelrtt30m" ON "steplog"'
    client.query(sql)
    sql='DROP CONTINUOUS QUERY "wans30m" ON "steplog"'
    client.query(sql)
    sql='DROP CONTINUOUS QUERY "pathtp30m" ON "steplog"'
    client.query(sql)
    sql='DROP CONTINUOUS QUERY "tunnelget30m" ON "steplog"'
    client.query(sql)
    sql='DROP CONTINUOUS QUERY "tunnel30m" ON "steplog"'
    client.query(sql)

if __name__ == "__main__"
    zcreate()
    #dclear()
    client.close()