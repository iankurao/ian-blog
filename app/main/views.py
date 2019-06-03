from flask_login import login_required


@main.route("/<uname>",methods=["GET","POST"])
@login_required
def new_pitch(uname):



@main.route("/pitch/new/review/<int:id>",methods=["GET","POST"])
@login_required
def review(id):


@main.route("/user/<uname>/update",methods=["GET","POST"])
@login_required
def update_profile(uname):    