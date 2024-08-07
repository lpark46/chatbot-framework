def message(request):
    answer = ((request.body).decode('utf-8'))
    json_str = json.loads(answer)

    # bot
    bot_id = json_str['bot']['id'] # "66b0895104d295078ba706a9!"
    bot_name = json_str['bot']['name'] # 피엔케이_챗봇_MASTER

    # intent
    intent_id = json_str['intent']['id'] # 66b3034b27bc5c0c5f6ce15a
    intent_name = json_str['intent']['name'] # testing_block_one
    intent_code = json_str['intent']['extra']['reason']['code'] # 0
    intent_message = json_str['intent']['extra']['reason']['message'] # "OK"

    # action
    action_id = json_str['action']['id'] # 66b300dc6a837c3df95dc7b1
    action_name = json_str['action']['name'] # return_test
    action_params = json_str['action']['params'] # 
        action_params = json_str['action']['params']['for_testing_greeting'] # 
    action_detailparams = json_str['action']['detailParams'] # 
    action_clientextra = json_str['action']['clientExtra'] # 

    # userRequest block
    userrequest_block_id = json_str['userRequest']['block']['id'] # 66b3034b27bc5c0c5f6ce15a
    userrequest_block_name = json_str['userRequest']['block']['name'] # testing_block_one
    
    # userRequest user
    # 동일한 사용자더라도 봇이 다르면 다른 id 발급
    userrequest_user_id = json_str['userRequest']['user']['id'] # 989d7d7fef108f826e046c333e8014acf0db60c6b637f6f6fdb17163a16b4e4be2
    userrequest_user_type = json_str['userRequest']['user']['type'] # botUserKey
    userrequest_user_properties_botuserkey = json_str['userRequest']['user']['properties']['botUserKey'] # 989d7d7fef108f826e046c333e8014acf0db60c6b637f6f6fdb17163a16b4e4be2
    userrequest_user_properties_bot_user_key = json_str['userRequest']['user']['properties']['bot_user_key'] # 989d7d7fef108f826e046c333e8014acf0db60c6b637f6f6fdb17163a16b4e4be2
    
    # userRequest
    userrequest_utterance = json_str['userRequest']['utterance'] # hello my good sir
    userrequest_params_ignoreme = json_str['userRequest']['params']['ignoreMe'] # true
    userrequest_params_surface = json_str['userRequest']['params']['surface'] # BuilderBotTest
    userrequest_lang = json_str['userRequest']['lang'] # ko
    userrequest_timezone = json_str['userRequest']['timezone'] # Asia/Seoul