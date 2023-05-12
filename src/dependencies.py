import aiohttp


async def task(word):
    pass


async def get_word_info(word):
    async with aiohttp.ClientSession() as session:
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        async with session.get(url.format(word=word)) as resp:
            response = await resp.json()

            data = []
            for word_info in response:
                audio_url = word_info.get("phonetics", ({},))[-1].get("audio", "")

                for meaning in word_info.get("meanings", ()):
                    word_ = {
                        "audio_url": audio_url,
                        "part_of_speech": meaning.get("partOfSpeech", ""),
                        "definitions": [],
                    }
                    # TODO here check in PartOfSpeech
                    for definition in meaning.get("definitions", ()):
                        definition_ = {
                            "text": definition.get("definition", ""),
                            "example": definition.get("example", ""),
                        }
                        word_["definitions"].append(definition_)
                    data.append(word_)

            return data
