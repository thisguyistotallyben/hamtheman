import socket
import threading
import discord


class DBotSocket:
    def __init__(self, bot, port):
        self.stats = {}
        self.bot = bot
        self.active = False

        # start the server
        t = threading.Thread(target=self.serve, args=(port,))
        t.start()

    def fill_stats(self, client):
        # servers and channels
        self.stats['servers'] = {}

        # get servers
        for i in client.guilds:
            sname = i.name
            self.stats['servers'][sname] = {}
            self.stats['servers'][sname]['id'] = i.id
            self.stats['servers'][sname]['channels'] = {}

            # get channels
            for j in i.channels:
                cname = j.name
                self.stats['servers'][sname]['channels'][cname] = j

        # set active


    def serve(self, port):
        print(f'serving on port {port}')
        HOST = ''
        PORT = port

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break

                        print('message received')
                        mess = data.decode()
                        msplit = mess.split(' ', 1)
                        command = msplit[0]

                        if command == 'list':
                            if len(msplit) == 2:
                                if msplit[1] == 'servers':
                                    ret = ''
                                    for i in self.stats['servers']:
                                        ret += i + '\n'
                                    conn.sendall(ret.encode())
                                elif msplit[1].startswith('from '):
                                    lsplit = msplit[1].split(' ', 1)
                                    if lsplit[1] in self.stats['servers']:
                                        ret = ''
                                        for i in self.stats['servers'][lsplit[1]]['channels']:
                                            ret += i + '\n'
                                        conn.sendall(ret.encode())
                        elif command == 'dothing':
                            print('doing the thing')
                            nmess = discord.Message
                            channel = self.stats['servers']['Young Hams']['channels']['general']
                            # await channel.send('hello')
                        else:
                            errmess = 'not a command'
                            conn.sendall(errmess.encode())
