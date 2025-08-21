from clean_talk_client.clean_talk_prediction_client import CleanTalkPredictionClient
from clean_talk_client.exception.clean_talk_exception import CleanTalkException
from clean_talk_client.kolas_ai_oauth_client import KolasAiOAuthClient
from clean_talk_client.message import Message
from clean_talk_client.predict_request import PredictRequest

YOUR_PROJECT_ID = ''  # Set your project ID
YOUR_CLIENT_ID = ''  # Set your client ID
YOUR_CLIENT_SECRET = ''  # Set your client secret


def main():
    try:
        oauth_client = KolasAiOAuthClient()
        auth_result = oauth_client.auth(YOUR_CLIENT_ID, YOUR_CLIENT_SECRET)
        print("Access token:", auth_result.access_token)
        print("Expires in:", auth_result.expires_in)

        # Example: Use the access token with your prediction client
        # from kolas_ai_prediction_client import CleanTalkPredictionClient, Message, PredictRequest
        client = CleanTalkPredictionClient(auth_result.access_token)
        request = PredictRequest(
            YOUR_PROJECT_ID,
            [
                Message('11177c92-1266-4817-ace5-cda430481111', 'Hello world!'),
                Message('22277c92-1266-4817-ace5-cda430482222', 'Good buy world!'),
            ]
        )
        # Sync request to kolas.ai. It returns result of predictions immediately
        response = client.predict(request)
        for prediction in response.get_predictions():
            print("MessageId:", prediction.message_id)
            print("Message:", prediction.message)
            print("Prediction:", prediction.prediction)
            print("Probability:", prediction.probability)
            print("Categories:", ", ".join(prediction.categories))

        # Async request to kolas.ai. Results of predictions will be sent on registered webhook
        client.async_predict(request)

    except CleanTalkException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
