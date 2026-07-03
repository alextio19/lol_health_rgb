def find_value(data, key):
    if not isinstance(data, dict):
        return None

    for found_key, value in data.items():
        if found_key == key:
            return value

        if isinstance(value, dict):
            result = find_value(value, key)
            if result is not None:
                return result

        elif isinstance(value, list):
            for item in value:
                result = find_value(item, key)
                if result is not None:
                    return result
    return None

def check_port(host, port):
    socket = __import__('socket')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10) 
    try:
        sock.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()