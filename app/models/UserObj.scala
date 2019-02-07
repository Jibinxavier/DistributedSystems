package models

import com.fasterxml.jackson.databind.JsonNode
import javax.inject.{Inject, Singleton}
import play.api.libs.json.JsValue
import play.libs.ws._

@Singleton
class UserObj @Inject()(val ws: WSClient) extends WSBodyReadables with WSBodyWritables{
   def signup(user: User): JsonNode= {
    // user could have already signed up
    // or user could be new
    //    println("The user name is " + userName + " password is " + password)
     var url = "http://127.0.0.1:8080/user/signup"

     val request: WSRequest = ws.url(url)
     val complexRequest: WSRequest = request.addHeader("Accept", "application/json")
     val futureResponse = complexRequest.post("user_name:" + user.userName + ",password:" + user.password)
     Thread.sleep(1000)


     futureResponse.toCompletableFuture.get().asJson()
  }
  def login(user: User): JsonNode ={
    var url = "http://127.0.0.1:8080/user/login"

    val request: WSRequest = ws.url(url)
    val complexRequest: WSRequest = request.addHeader("Accept", "application/json")
    val futureResponse = complexRequest.post("user_name:" + user.userName + ",password:" + user.password)
    Thread.sleep(1000)


    return futureResponse.toCompletableFuture.get().asJson()
  }
}