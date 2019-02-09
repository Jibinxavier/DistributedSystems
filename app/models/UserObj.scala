package models

import com.fasterxml.jackson.databind.JsonNode
import javax.inject.{Inject, Singleton}
import play.libs.ws._
@Singleton
class UserObj @Inject()(val ws: WSClient) extends WSBodyReadables with WSBodyWritables{
   def signup(user: User): JsonNode= {
    // user could have already signed up
    // or user could be new
    //    println("The user name is " + userName + " password is " + password)
     var url = "http://127.0.0.1:8080/user/signup"

     return userdbConnector(url, user.toJsonString())
  }


  def login(user: User): JsonNode ={


    var url = "http://127.0.0.1:8080/user/login"


    return userdbConnector(url, user.toJsonString())
  }
  def userdbConnector(endpoint: String, data: String): JsonNode = {


    val request: WSRequest = ws.url(endpoint)
    val complexRequest: WSRequest = request.addHeader("Accept", "application/json")

    val futureResponse = complexRequest.post(data)
    Thread.sleep(1000)


    return futureResponse.toCompletableFuture.get().asJson()
  }
}