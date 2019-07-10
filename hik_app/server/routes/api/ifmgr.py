from hik_app import app

app.route('/ISAPI/Ifmgr/Interfaces', methods=['SET'])
def ifmgr_interfaces_set(request):
    body = request.body




