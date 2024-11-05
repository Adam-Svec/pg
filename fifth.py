import sys

jpeg_header = b'\xff\xd8'
gif_headers = [b'GIF87a', b'GIF89a']
png_header = b'\x89PNG\r\n\x1a\n'

def read_header(file_name, header_length):
    try:
        with open(file_name, "rb") as file:
            return file.read(header_length)
    except FileNotFoundError:
        raise Exception(f"Soubor '{file_name}' nenalezen.")
    except Exception as e:
        raise Exception(f"Chyba: {e}")

def is_jpeg(header):
    return header.startswith(jpeg_header)

def is_gif(header):
    return any(header.startswith(gif) for gif in gif_headers)

def is_png(header):
    return header.startswith(png_header)

def print_file_type(file_name):
    header = read_header(file_name, max(len(jpeg_header), len(gif_headers[0]), len(png_header)))
    
    if is_jpeg(header):
        print(f'Soubor {file_name} je JPEG.')
    elif is_gif(header):
        print(f'Soubor {file_name} je GIF.')
    elif is_png(header):
        print(f'Soubor {file_name} je PNG.')
    else:
        print(f'Soubor {file_name}  neznámý.')

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except IndexError:
        print("Chyba: název souboru.")
    except Exception as e:
        print(f"Chyba: {e}")