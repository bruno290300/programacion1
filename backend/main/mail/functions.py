from .. import mailsender
from flask import current_app, render_template, Blueprint
from flask_mail import Message
from smtplib import SMTPException
from main.models import UsuarioModel, BolsonModel
from main.auth.decoradores import admin_required
def sendMail(to, subject, template, **kwargs):
    #Configuracion del mail
    msg = Message( subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=to)
    try:

        msg.body = render_template(template + '.txt', **kwargs)
        """msg.html = render_template(template + '.html', **kwargs)"""

        result = mailsender.send(msg)
    except SMTPException as e:
        print(str(e))
        return "Mail deliver failed"
    return True

mail = Blueprint('mail', __name__, url_prefix='/mail')

@mail.route('/promocion', methods=['POST'])
@admin_required
def promocion():
    usuarios = db.session.query(UsuarioModel).filter(UsuarioModel.role == 'cliente').all()
    bolsonesVenta = db.session.query(BolsonModel).filter(BolsonModel.aprobado == 1).all()
    try:
        for usuario in usuarios:
            sent = sendMail([usuario.mail], "Ofertas de la semana", 'promo', usuario = usuario, bolsones = [bolson.nombre for bolson in bolsonesVenta])
    except SMTPException as e:
        print(str(e))
        return "Mail deliver failed"
    return 'mails sent', 200

