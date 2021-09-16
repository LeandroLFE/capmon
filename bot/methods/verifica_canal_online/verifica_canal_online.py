async def verifica_canal_online(self, dados):
    _aux_stream = await self.bot._http.get_streams(user_ids = [dados['canal_id']])
    get_stream = [{'type': 'None'}] if _aux_stream == [] else _aux_stream
    get_stream = get_stream[0]
    _stream_online = True if get_stream['type'] == 'live' else False
    return _stream_online