from Model import db_connection
from Model import db_query
from fastapi.responses import JSONResponse

engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close  = db_query.db_close

def pre_get_all():

    try:
        result = db_query.db_newsdata_get()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == []:
            result = JSONResponse(status_code=404, content="Data Not Found")

    finally:
        session.close()

    return result

def pre_get_list():

    try:
        result = db_query.db_newslist_get()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == []:
            result = JSONResponse(status_code=404, content="Data Not Found")

    finally:
        session.close()

    return result

def pre_post_list(addlist):

    try:
        db_query.db_newslink_post(addlist)
        commit()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        result = JSONResponse(status_code=200, content="OK")

    finally:
        session.close()

    return result

def pre_get_newsdata(news):

    try:
        result = db_query.db_newsdata_get_news(news)

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == []:
            result = JSONResponse(status_code=404, content="Data Not Found")

    finally:
        session.close()

    return result

def pre_get_date(date):

    try:
        result = db_query.db_newsdata_get_date(date)

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == []:
            result = JSONResponse(status_code=404, content="Data Not Found")

    finally:
        session.close()

    return result

def pre_del_all():

    try:
        result = db_query.db_newsdata_del_all()
        session.commit()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == 0:
            result = JSONResponse(status_code=404, content="Data Not Found")

        else:
            result = JSONResponse(status_code=200, content="200 OK")

    finally:
        session.close()

    return result

def pre_patch_list(patchlist,id):

    try:
        db_query.db_newslist_patch(patchlist,id)
        commit()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        result = JSONResponse(status_code=200, content="OK")

    finally:
        session.close()

    return result

def pre_post_subscribe(email):

    try:
        db_query.db_subscribe_email()
        commit()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        result = JSONResponse(status_code=200, content="OK")

    finally:
        session.close()

    return result