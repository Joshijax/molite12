function createModal(title, message, type) {
    customModal(title, message, type);
}

function customModal(head, body, type) {
    if (type == 'prompt') {
        $('#modal-head').html('<h4 class="modal-title">' + head + '</h4>');
        $('#modal-body').html('<div class="row"><label class="col-sm-3">Name</label> <div class="col-md-9">  <input class="form-control" type="text" id="name-input">  </div>  </div>');
        $('#modal-footer').html('<button type="button" class="btn btn-primary" id="done-btn">Done</button>  <button type="button" class="btn btn-danger" id="cancel-btn">Cancel</button>');
        $('#custom-modal').modal('show');
        $('#cancel-btn').on('click', function() {
            return response('cancel');
        });
        $('#done-btn').on('click', function() {
            return response('done');
        });
    } else if (type == 'alert') {
        $('#modal-head').html('<h4 class="modal-title">' + head + '</h4>');
        $('#modal-body').html('<p>' + body + '</p>');
        $('#modal-footer').html('<button type="button" class="btn btn-primary" data-dismiss="modal">Ok</button>');
        $('#custom-modal').modal('show');
    } else if (type == 'confirm') {
        $('#modal-head').html('<h4 class="modal-title">' + head + '</h4>');
        $('#modal-body').html('<p>' + body + '</p>');
        $('#modal-footer').html('<button type="button" class="btn btn-primary" id="ok-btn">Ok</button>/  <button type="button" class="btn btn-danger" id="cancel-btn">Cancel</button>');
        $('#custom-modal').modal('show');
        $('#cancel-btn').on('click', function() {
            return response('cancel');
        });
        $('#ok-btn').on('click', function() {
            return response('ok');
        });
    }
}

function response(type) {
    if (type == 'done') {
        if (document.getElementById('name-input').value != '') {
            $('#user-name').html('Welcome ' + document.getElementById('name-input').value);
            $('#custom-modal').modal('hide');
            return document.getElementById('name-input').value;
        } else {
            alert('Please Enter your name');
        }
    } else if (type == 'cancel') {
        $('#custom-modal').modal('hide');
        return false;
    } else if (type == 'ok') {
        $('#custom-modal').modal('hide');
        return true;
    }
}

function createModal(title, message, type) {
    customModal(title, message, type);
}

function customModal(head, body, type) {
    if (type == 'prompt') {
        $('#modal-head').html('<h4 class="modal-title">' + head + '</h4>');
        $('#modal-body').html('<div class="row"><label class="col-sm-3">Name</label> <div class="col-md-9">  <input class="form-control" type="text" id="name-input">  </div>  </div>');
        $('#modal-footer').html('<button type="button" class="btn btn-primary" id="done-btn">Done</button>  <button type="button" class="btn btn-danger" id="cancel-btn">Cancel</button>');
        $('#custom-modal').modal('show');
        $('#cancel-btn').on('click', function() {
            return response('cancel');
        });
        $('#done-btn').on('click', function() {
            return response('done');
        });
    } else if (type == 'alert') {
        $('#modal-head').html('<h4 class="modal-title">' + head + '</h4>');
        $('#modal-body').html('<p>' + body + '</p>');
        $('#modal-footer').html('<button type="button" class="btn btn-primary" data-dismiss="modal">Ok</button>');
        $('#custom-modal').modal('show');
    } else if (type == 'confirm') {
        $('#modal-head').html('<h4 class="modal-title">' + head + '</h4>');
        $('#modal-body').html('<p>' + body + '</p>');
        $('#modal-footer').html('<button type="button" class="btn btn-primary" id="ok-btn">Ok</button>/  <button type="button" class="btn btn-danger" id="cancel-btn">Cancel</button>');
        $('#custom-modal').modal('show');
        $('#cancel-btn').on('click', function() {
            return response('cancel');
        });
        $('#ok-btn').on('click', function() {
            return response('ok');
        });
    }
}

function response(type) {
    if (type == 'done') {
        if (document.getElementById('name-input').value != '') {
            $('#user-name').html('Welcome ' + document.getElementById('name-input').value);
            $('#custom-modal').modal('hide');
            return document.getElementById('name-input').value;
        } else {
            alert('Please Enter your name');
        }
    } else if (type == 'cancel') {
        $('#custom-modal').modal('hide');
        return false;
    } else if (type == 'ok') {
        $('#custom-modal').modal('hide');
        return true;
    }
}