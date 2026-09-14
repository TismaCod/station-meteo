logs = [
    "192.168.1.10;LOGIN;FAIL",
    "192.168.1.11;LOGIN;SUCCESS",
    "192.168.1.20;LOGIN;FAIL",
    "192.168.1.20;LOGIN;FAIL",
    "192.168.1.20;LOGIN;FAIL",
    "192.168.1.30;LOGIN;SUCCESS",
    "192.168.1.40;LOGIN;FAIL",
    "192.168.1.40;LOGIN;FAIL",
    "192.168.1.40;LOGIN;FAIL",
    "192.168.1.50;SCAN;DETECTED"]

def scan_detected(n):
        compteur = 0
        for i in logs:
              ip,action,status = i.split(';')
              if ip == n and action == 'SCAN':
                     compteur += 1
        return compteur    

total_scan = 0
list_scan = []
for i in logs:
        ip,action,status = i.split(';')
        if scan_detected(ip) > 0 and ip not in list_scan:
               list_scan.append(ip)
               total_scan += scan_detected(ip)

def ip_success(n):
        compteur = 0
        for i in logs:
              ip,action,status = i.split(';')
              if ip == n and status == 'SUCCESS':
                     compteur += 1
        return compteur

total_success = 0
list_success = []
for i in logs:
        ip,action,status = i.split(';')
        if ip_success(ip) > 0 and ip not in list_success:
               list_success.append(ip)
               total_success += ip_success(ip)
print("TOTAL SUCCES : ",total_success)

def ip_fail(n):
        compteur = 0
        for i in logs:
              ip,action,status = i.split(';')
              if ip == n and status == 'FAIL':
                     compteur += 1
        return compteur

total_fail = 0
list_fail = []
ip_alerte = []
for i in logs:
        ip,action,status = i.split(';')
        if ip_fail(ip) > 0 and ip not in list_fail:
               list_fail.append(ip)
               total_fail += ip_fail(ip)
        if ip_fail(ip) >= 3 and ip not in ip_alerte:
               ip_alerte.append(ip)
print("TOTAL FAIL : ",total_fail)
for ip in list_fail:
       print(ip, ip_fail(ip))

if ip_alerte:
       print("!!!!! ALERTE DE SECURITE !!!!!\n")
       for ip in ip_alerte:
              print("IP Suspecte : ",ip," -> ",ip_fail(ip),"alertes")

print("\n\n===== RAPPORT =====\n\n","Nombre d'evenement : ",len(logs),"\nConnexion reussies : ",total_success,"\nConnexions echouees : ",total_fail,"\nScans detectes : ",total_scan,"\nIPs suspectes : ",ip_alerte)
