package models
import javax.inject.{Inject, Singleton}
import play.libs.ws._
import play.api.Configuration
import services.Encryption

/*
  This object will be used to talk to user database which has an interface written in python
 */
@Singleton
class UserDBConnector @Inject()(val ws: WSClient, config: Configuration, encryptor: Encryption) extends WSBodyReadables with WSBodyWritables{
   def signup(user: User): String= {
    // user could have already signed up
    // or user could be new
    //    println("The user name is " + userName + " password is " + password)

     val url =  "%s/user/signup".format( config.get[String]("pythonDb"))

     return userdbConnector(url, user.toJsonString())
  }


  def login(user: User): String ={


    var url = "%s/user/login".format( config.get[String]("pythonDb"))
    // TODO parse the response and add tokenGenerator()s

    return userdbConnector(url, user.toJsonString())
  }

  def userdbConnector(endpoint: String, data: String): String = {


    val request: WSRequest = ws.url(endpoint)
    val complexRequest: WSRequest = request.addHeader("Accept", "application/json")

    val futureResponse = complexRequest.post(data)
    Thread.sleep(1000)

    return futureResponse.toCompletableFuture.get().asJson().toString()
  }
}