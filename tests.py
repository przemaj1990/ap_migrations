from ntc_templates.parse import parse_output
import textfsm
output = """

Number of APs.................................... 4135

Global AP User Name.............................. hold
Global AP Dot1x User Name........................ Not Configured

AP Name             Slots  AP Model              Ethernet MAC       Location          Country     IP Address       Clients   DSE Location
------------------  -----  --------------------  -----------------  ----------------  ----------  ---------------  --------  --------------
DK-HHS-AP-045        2     AIR-CAP2602I-E-K9     b8:38:61:24:f5:e3  Hedehusene, Term  DK          10.45.147.24       3       [0 ,0 ,0 ]
DK-HOR-AP-009        2     AIR-LAP1142N-E-K9     70:ca:9b:15:2a:dc  Horsens           DK          10.45.42.80        1       [0 ,0 ,0 ]
DE-KRE-AP-085        2     AIR-CAP2702I-E-K9     a8:9d:21:27:ce:9c  Krefeld           DK          10.49.190.47       0       [0 ,0 ,0 ]
SE-HEL-AP-01         2     AIR-CAP2702I-E-K9     84:3d:c6:07:03:cc  default location  DK          10.46.236.238      0       [0 ,0 ,0 ]
DK-HOR-AP-142        2     AIR-LAP1142N-E-K9     64:9e:f3:2f:7a:a3  Horsens           DK          10.45.40.27        3       [0 ,0 ,0 ]
DK-HOR-AP-107        2     AIR-LAP1142N-E-K9     70:ca:9b:15:28:e9  Horsens           DK          10.45.42.28        0       [0 ,0 ,0 ]
DK-HOR-AP-084        2     AIR-LAP1142N-E-K9     70:ca:9b:28:b1:12  Horsens           DK          10.45.42.13        0       [0 ,0 ,0 ]
SE-MST-AP-33         1     AIR-LAP1141N-E-K9     70:ca:9b:6b:48:06  Marsta            DK          10.46.71.53        2       [0 ,0 ,0 ]
DK-HOR-AP-117        2     AIR-LAP1142N-E-K9     70:ca:9b:28:b1:3d  Horsens           DK          10.45.42.107       0       [0 ,0 ,0 ]
DK-HOR-AP-143        2     AIR-LAP1142N-E-K9     64:9e:f3:4d:c8:32  Horsens           DK          10.45.40.102       2       [0 ,0 ,0 ]
AP5057.a84e.52ff     1     AIR-LAP1141N-E-K9     50:57:a8:4e:52:ff  LAA Warehouse A0  DK          10.46.177.73       1       [0 ,0 ,0 ]
PL-PEC-AP-22         2     AIR-CAP2702I-E-K9     40:ce:24:d4:be:08  default location  DK          10.48.124.239      11      [0 ,0 ,0 ]
NO-LST-AP-19         2     AIR-LAP1142N-E-K9     70:81:05:07:43:06  Lillestrom        DK          10.47.22.22        0       [0 ,0 ,0 ]
SE-BOR-AP-116        2     AIR-CAP2702I-E-K9     f8:0b:cb:26:a0:00  Boras             SE          10.46.133.149      0       [0 ,0 ,0 ]
DE-KRE-AP-080        2     AIR-CAP2702I-E-K9     74:a2:e6:8d:39:78  Krefeld           DK          10.49.207.26       3       [0 ,0 ,0 ]
DE-WWI03-AP-16       2     AIR-CAP2702I-E-K9     00:81:c4:8d:f2:48  Weilerswist       DK          10.49.112.66       0       [0 ,0 ,0 ]
DE-LHC-AP-10         2     AIR-CAP2702I-E-K9     1c:6a:7a:b3:5b:b4  Langenbach        DE          10.49.248.86       5       [0 ,0 ,0 ]
DE-LHC-AP-26         2     AIR-CAP2702I-E-K9     1c:6a:7a:b3:5b:ec  Langenbach        DE          10.49.248.73       0       [0 ,0 ,0 ]
DE-LEJ-AP-21         1     AIR-LAP1141N-E-K9     10:f3:11:9a:37:93  DE-Leipzig        DK          10.49.96.35        0       [0 ,0 ,0 ]
DE-WWI03-AP-19       2     AIR-CAP2702I-E-K9     00:2a:10:34:0f:c8  Weilerswist       DK          10.49.112.69       10      [0 ,0 ,0 ]
DE-KRE-AP-137        2     AIR-CAP2702I-E-K9     a8:9d:21:27:cf:ec  Krefeld           DK          10.49.190.54       5       [0 ,0 ,0 ]
DK-HHS-AP-025        2     AIR-CAP2602I-E-K9     b8:38:61:27:87:dd  Hedehusene, Term  DK          10.45.147.219      5       [0 ,0 ,0 ]
PL-PEC-AP-23         2     AIR-CAP2702I-E-K9     70:df:2f:d3:9a:30  default location  DK          10.48.124.242      3       [0 ,0 ,0 ]
SE-BOR-AP-50         2     AIR-CAP2702E-E-K9     78:72:5d:b0:48:e0  Boras             DK          10.46.133.82       1       [0 ,0 ,0 ]
SE-LAA-AP-025        1     AIR-LAP1141N-E-K9     50:57:a8:30:37:f5  LAA Warehouse A0  DK          10.46.177.83       0       [0 ,0 ,0 ]
SE-LAA-AP-034        1     AIR-LAP1141N-E-K9     50:57:a8:4e:53:31  LAA Warehouse A0  DK          10.46.177.12       1       [0 ,0 ,0 ]
SE-BOR-AP-25         2     AIR-CAP2702E-E-K9     50:2f:a8:99:a8:5c  Boras             DK          10.46.133.13       0       [0 ,0 ,0 ]
DK-HOR-AP-058        2     AIR-LAP1142N-E-K9     cc:ef:48:c2:33:5c  Horsens           DK          10.45.42.24        0       [0 ,0 ,0 ]
BE-PUU02-AP-02       2     AIR-CAP2702I-E-K9     b0:26:80:98:53:78  Puurs, Solutions  DK          10.32.214.105      12      [0 ,0 ,0 ]
SE-LAA-AP-130        1     AIR-LAP1261N-E-K9     6c:20:56:49:09:d9  LAA Warehouse A0  DK          10.46.177.115      0       [0 ,0 ,0 ]
SE-BOR-AP-97         2     AIR-CAP2702I-E-K9     d4:c9:3c:df:ac:f4  Boras             DK          10.46.133.138      0       [0 ,0 ,0 ]
SE-LAA-AP-014        1     AIR-LAP1141N-E-K9     44:2b:03:1f:c2:7f  LAA Warehouse A0  DK          10.46.177.65       4       [0 ,0 ,0 ]
NO-LST-AP-01         2     AIR-CAP2702I-E-K9     f0:7f:06:d7:a1:b0  Lillestrom        DK          10.47.26.33        0       [0 ,0 ,0 ]
DK-HOR-AP-012        2     AIR-LAP1142N-E-K9     64:9e:f3:4d:c7:c3  Horsens           DK          10.45.42.39        1       [0 ,0 ,0 ]
DE-KRE-AP-096        2     AIR-CAP2702I-E-K9     64:f6:9d:99:aa:90  Krefeld           DK          10.49.190.124      1       [0 ,0 ,0 ]
DE-LHC-AP-28         2     AIR-CAP2702I-E-K9     1c:6a:7a:ac:07:c0  Langenbach        DE          10.49.248.74       0       [0 ,0 ,0 ]
SE-LAA-AP-066        2     AIR-LAP1142N-E-K9     2c:54:2d:8e:e1:5d  LAA Office A01-2  DK          10.46.178.18       1       [0 ,0 ,0 ]

"""


command = "show ap summary"



new_output = parse_output(platform="cisco_wlc_ssh", command="show ap summary", data=output)
# new_output = textfsm.TextFSM(output)

print(new_output)

new_output2 = [{
    'ip': '10.45.147.24',
    'mac': 'b8:38:61:24:f5:e3',
    'country': 'DK',
    'location': 'Hedehusene, Term',
    'ap_name': 'DK-HHS-AP-045',
    'slot': '2', 'ap_model':'AIR-CAP2602I-E-K9',
    'dse_location': '[0 ,0 ,0 ]',
    'clients': '3'},

    {'ip': '10.45.42.80',
     'mac': '70:ca:9b:15:2a:dc',
     'country': 'DK',
     'location': 'Horsens',
     'ap_name': 'DK-HOR-AP-009',
     'slot': '2', 'ap_model': 'AIR-LAP1142N-E-K9',
     'dse_location': '[0 ,0 ,0 ]',
     'clients': '1'},

    {'ip': '10.49.190.47',
     'mac': 'a8:9d:21:27:ce:9c',
     'country': 'DK',
     'location': 'Krefeld',
     'ap_name': 'DE-KRE-AP-085',
     'slot': '2',
     'ap_model': 'AIR-CAP2702I-E-K9',
     'dse_location': '[0 ,0 ,0 ]',
     'clients': '0'},

    {'ip': '10.46.236.238',
     'mac': '84:3d:c6:07:03:cc',
     'country': 'DK',
     'location': 'default location',
     'ap_name': 'SE-HEL-AP-01',
     'slot': '2',
     'ap_model': 'AIR-CAP2702I-E-K9',
     'dse_location': '[0 ,0 ,0 ]',
     'clients': '0'},

    {'ip': '10.45.40.27',
     'mac': '64:9e:f3:2f:7a:a3',
     'country': 'DK',
     'location': 'Horsens',
     'ap_name': 'DK-HOR-AP-142',
     'slot': '2',
     'ap_model': 'AIR-LAP1142N-E-K9',
     'dse_location': '[0 ,0 ,0 ]',
     'clients': '3'},

    {'ip': '10.45.42.28',
     'mac': '70:ca:9b:15:28:e9',
     'country': 'DK',
     'location': 'Horsens',
     'ap_name': 'DK-HOR-AP-107',
     'slot': '2',
     'ap_model': 'AIR-LAP1142N-E-K9',
     'dse_location': '[0 ,0 ,0 ]',
     'clients': '0'},

    {'ip': '10.45.42.13',
     'mac': '70:ca:9b:28:b1:12',
     'country': 'DK',
     'location': 'Horsens',
     'ap_name': 'DK-HOR-AP-084',
     'slot': '2',
     'ap_model': 'AIR-LAP1142N-E-K9',
     'dse_location': '[0 ,0 ,0 ]',
     'clients': '0'},

    {'ip': '10.46.71.53', 'mac': '70:ca:9b:6b:48:06', 'country': 'DK', 'location': 'Marsta', 'ap_name': 'SE-MST-AP-33', 'slot': '1', 'ap_model': 'AIR-LAP1141N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '2'}, {'ip': '10.45.42.107', 'mac': '70:ca:9b:28:b1:3d', 'country': 'DK', 'location': 'Horsens', 'ap_name': 'DK-HOR-AP-117', 'slot': '2', 'ap_model': 'AIR-LAP1142N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.45.40.102', 'mac': '64:9e:f3:4d:c8:32', 'country': 'DK', 'location': 'Horsens', 'ap_name': 'DK-HOR-AP-143', 'slot': '2', 'ap_model': 'AIR-LAP1142N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '2'}, {'ip': '10.46.177.73', 'mac': '50:57:a8:4e:52:ff', 'country': 'DK', 'location': 'LAA Warehouse A0', 'ap_name': 'AP5057.a84e.52ff', 'slot': '1', 'ap_model': 'AIR-LAP1141N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '1'}, {'ip': '10.48.124.239', 'mac': '40:ce:24:d4:be:08', 'country': 'DK', 'location': 'default location', 'ap_name': 'PL-PEC-AP-22', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '11'}, {'ip': '10.47.22.22', 'mac': '70:81:05:07:43:06', 'country': 'DK', 'location': 'Lillestrom', 'ap_name': 'NO-LST-AP-19', 'slot': '2', 'ap_model': 'AIR-LAP1142N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.46.133.149', 'mac': 'f8:0b:cb:26:a0:00', 'country': 'SE', 'location': 'Boras', 'ap_name': 'SE-BOR-AP-116', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.49.207.26', 'mac': '74:a2:e6:8d:39:78', 'country': 'DK', 'location': 'Krefeld', 'ap_name': 'DE-KRE-AP-080', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '3'}, {'ip': '10.49.112.66', 'mac': '00:81:c4:8d:f2:48', 'country': 'DK', 'location': 'Weilerswist', 'ap_name': 'DE-WWI03-AP-16', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.49.248.86', 'mac': '1c:6a:7a:b3:5b:b4', 'country': 'DE', 'location': 'Langenbach', 'ap_name': 'DE-LHC-AP-10', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '5'}, {'ip': '10.49.248.73', 'mac': '1c:6a:7a:b3:5b:ec', 'country': 'DE', 'location': 'Langenbach', 'ap_name': 'DE-LHC-AP-26', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.49.96.35', 'mac': '10:f3:11:9a:37:93', 'country': 'DK', 'location': 'DE-Leipzig', 'ap_name': 'DE-LEJ-AP-21', 'slot': '1', 'ap_model': 'AIR-LAP1141N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.49.112.69', 'mac': '00:2a:10:34:0f:c8', 'country': 'DK', 'location': 'Weilerswist', 'ap_name': 'DE-WWI03-AP-19', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '10'}, {'ip': '10.49.190.54', 'mac': 'a8:9d:21:27:cf:ec', 'country': 'DK', 'location': 'Krefeld', 'ap_name': 'DE-KRE-AP-137', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '5'}, {'ip': '10.45.147.219', 'mac': 'b8:38:61:27:87:dd', 'country': 'DK', 'location': 'Hedehusene, Term', 'ap_name': 'DK-HHS-AP-025', 'slot': '2', 'ap_model': 'AIR-CAP2602I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '5'}, {'ip': '10.48.124.242', 'mac': '70:df:2f:d3:9a:30', 'country': 'DK', 'location': 'default location', 'ap_name': 'PL-PEC-AP-23', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '3'}, {'ip': '10.46.133.82', 'mac': '78:72:5d:b0:48:e0', 'country': 'DK', 'location': 'Boras', 'ap_name': 'SE-BOR-AP-50', 'slot': '2', 'ap_model': 'AIR-CAP2702E-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '1'}, {'ip': '10.46.177.83', 'mac': '50:57:a8:30:37:f5', 'country': 'DK', 'location': 'LAA Warehouse A0', 'ap_name': 'SE-LAA-AP-025', 'slot': '1', 'ap_model': 'AIR-LAP1141N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.46.177.12', 'mac': '50:57:a8:4e:53:31', 'country': 'DK', 'location': 'LAA Warehouse A0', 'ap_name': 'SE-LAA-AP-034', 'slot': '1', 'ap_model': 'AIR-LAP1141N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '1'}, {'ip': '10.46.133.13', 'mac': '50:2f:a8:99:a8:5c', 'country': 'DK', 'location': 'Boras', 'ap_name': 'SE-BOR-AP-25', 'slot': '2', 'ap_model': 'AIR-CAP2702E-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.45.42.24', 'mac': 'cc:ef:48:c2:33:5c', 'country': 'DK', 'location': 'Horsens', 'ap_name': 'DK-HOR-AP-058', 'slot': '2', 'ap_model': 'AIR-LAP1142N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.32.214.105', 'mac': 'b0:26:80:98:53:78', 'country': 'DK', 'location': 'Puurs, Solutions', 'ap_name': 'BE-PUU02-AP-02', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '12'}, {'ip': '10.46.177.115', 'mac': '6c:20:56:49:09:d9', 'country': 'DK', 'location': 'LAA Warehouse A0', 'ap_name': 'SE-LAA-AP-130', 'slot': '1', 'ap_model': 'AIR-LAP1261N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.46.133.138', 'mac': 'd4:c9:3c:df:ac:f4', 'country': 'DK', 'location': 'Boras', 'ap_name': 'SE-BOR-AP-97', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.46.177.65', 'mac': '44:2b:03:1f:c2:7f', 'country': 'DK', 'location': 'LAA Warehouse A0', 'ap_name': 'SE-LAA-AP-014', 'slot': '1', 'ap_model': 'AIR-LAP1141N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '4'}, {'ip': '10.47.26.33', 'mac': 'f0:7f:06:d7:a1:b0', 'country': 'DK', 'location': 'Lillestrom', 'ap_name': 'NO-LST-AP-01', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.45.42.39', 'mac': '64:9e:f3:4d:c7:c3', 'country': 'DK', 'location': 'Horsens', 'ap_name': 'DK-HOR-AP-012', 'slot': '2', 'ap_model': 'AIR-LAP1142N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '1'}, {'ip': '10.49.190.124', 'mac': '64:f6:9d:99:aa:90', 'country': 'DK', 'location': 'Krefeld', 'ap_name': 'DE-KRE-AP-096', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '1'}, {'ip': '10.49.248.74', 'mac': '1c:6a:7a:ac:07:c0', 'country': 'DE', 'location': 'Langenbach', 'ap_name': 'DE-LHC-AP-28', 'slot': '2', 'ap_model': 'AIR-CAP2702I-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '0'}, {'ip': '10.46.178.18', 'mac': '2c:54:2d:8e:e1:5d', 'country': 'DK', 'location': 'LAA Office A01-2', 'ap_name': 'SE-LAA-AP-066', 'slot': '2', 'ap_model': 'AIR-LAP1142N-E-K9', 'dse_location': '[0 ,0 ,0 ]', 'clients': '1'}]
