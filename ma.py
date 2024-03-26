import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor de correo
smtp_server = 'smtp-relay.brevo.com'
port = 587 # o usa 465 para SSL
username = 'trapapedevelopment@gmail.com'
password = 'xsmtpsib-0578a599165e5a89664617eab4129496e30e27550d27af96547131245fe41144-vEIcaJ95s01MLTfX'
from_addr = 'administrador@trapape.mx'
to_addrs = ['estres@trapape.mx']  # Cambia esto por tus direcciones de prueba

# Mensaje de correo
subject = 'Prueba de Estres'
body = 'Este es el cuerpo del mensaje de correo electrónico de prueba.'

# Crea una sesión SMTP y envía el correo
try:
    # Establece conexión con el servidor
    server = smtplib.SMTP(smtp_server, port)
    #server.starttls()  # Comentar si se usa SSL
    server.login(username, password)
    
    for i in range(100):  # Número de correos a enviar, ajustar según sea necesario
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = ", ".join(to_addrs)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server.sendmail(from_addr, to_addrs, msg.as_string())
        print(f'Correo {i+1} enviado')

    server.quit()
    print('Prueba de estres completada exitosamente.')
except Exception as e:
    print('Error:', e)
