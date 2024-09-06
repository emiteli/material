from PIL import Image
import qrcode

a4_width, a4_height = (2480, 3508)

columns = 14  
rows = 20  
qr_size = 150  
padding = 20  

def generate_qr(data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

def generate_qr_sheet(prefix, start_suffix, qr_count, filename):
    a4_image = Image.new("RGB", (a4_width, a4_height), "white")
    
    current_suffix = start_suffix
    for row in range(rows):
        for col in range(columns):
            if current_suffix > start_suffix + qr_count - 1:
                break

            qr_code = f"{prefix}{current_suffix}"
            qr_img = generate_qr(qr_code)
            qr_img = qr_img.resize((qr_size, qr_size))
            
            x = col * (qr_size + padding) + padding
            y = row * (qr_size + padding) + padding
            
            a4_image.paste(qr_img, (x, y))
            
            current_suffix += 1

    a4_image.save(filename)

prefix = "00114150108240"
# Gerando a primeira folha (280 QR codes)
start_suffix = 2501
generate_qr_sheet(prefix, start_suffix, 280, "C:\Archlinux\CriandoQRCodePython\qrcodes_sheet_1.png")
# Gerando a segunda folha (220 QR codes restantes)
start_suffix += 280
generate_qr_sheet(prefix, start_suffix, 220, "C:\Archlinux\CriandoQRCodePython\qrcodes_sheet_2.png")
