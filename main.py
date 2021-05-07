import asyncio
import datetime
import websockets
import json


# 클라이언트 접속이 되면 호출된다.
async def accept(websocket, path):
    while True:
        await asyncio.sleep(1.0);
        # 클라이언트로부터 메시지를 대기한다.
        data = {"0":1}
        # 클라인언트로 echo를 붙여서 재 전송한다.
        await websocket.send(json.dumps(data));



# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다.
start_server = websockets.serve(accept, "localhost", 9998);

# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever();
