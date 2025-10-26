
from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itinry_chain import gen_iti          
from utils.custom_exception import CustomException
from utils.logger import get_logger

logger = get_logger(__name__)

class TravelAssist:
    def __init__(self):
        self.msg = []
        self.city = ""
        self.interest= []
        self.inti=""

    def set_city(self, city):
        try:
            self.city = city
            self.msg.append(HumanMessage(content=city))
        except Exception as e:
            raise CustomException("Failed in City", e)
    
    def set_interest(self,interest_list):
        try:
            self.interest = [i.strip() for i in interest_list.split(",")]
            self.msg.append(HumanMessage(content=interest_list))
        except Exception as e:
            raise CustomException("Failed Interest", e)
    
    def create_init(self):
        try:
            self.inti = gen_iti(self.city,self.interest)
            self.msg.append(AIMessage(content=self.inti))
            return self.inti
        except Exception as e:
            raise CustomException("Failed to get Inti", e)