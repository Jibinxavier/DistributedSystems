package controllers

import javax.inject.Inject
import models.{User, UserDBConnector}
import play.api.mvc.{AbstractController, ControllerComponents, Request}
import play.api.libs.json._
import services.Encryption

class AuthenticationController @Inject()(cc: ControllerComponents,   userDao: UserDBConnector, encryptor: Encryption) extends AbstractController(cc) {


  def signUp = Action { request =>
    request.body.asJson.map { json =>
      json.validate[(String, String)].map {
        case (userName, password) =>
          val result = Json.toJson( userDao.signup(new User(userName, password)))
          Ok(result)
        case _ =>  BadRequest("Detected error:")
      }.recoverTotal {
        e => BadRequest("Detected error:" + JsError.toJson(e))
      }
    }.getOrElse {
      BadRequest("Expecting Json data")
    }
  }


  def login = Action { request =>
    request.body.asJson.map { json =>
      json.validate[(String, String)].map {
        case (userName, password) =>
          val result = userDao.login(new User(userName, password))

          val token = encryptor.tokenGenerator()
          if (result("code") == "1") {
            val token = encryptor.tokenGenerator()
            Ok(  Json.toJson(result) ).withSession(
                   "sessionId" -> token("sessionId"),  "sessionExpiryTM"->token("sessionExpiryTM"))

          }
          else {
            Ok(  Json.toJson(result) ).withNewSession
          }

//          Ok (  Json.toJson(result)  ).withSession(
//            "sessionId" -> token("sessionId"),  "sessionExpiryTM"->token("sessionExpiryTM"))
        case _ =>  BadRequest("Detected error:")

      }.recoverTotal {
        e => BadRequest("Detected error:" + JsError.toJson(e))
      }
    }.getOrElse {
      BadRequest("Expecting Json data")
    }
  }


  def logout = Action {
    Ok("Successfully signed out").withNewSession
  }

}
