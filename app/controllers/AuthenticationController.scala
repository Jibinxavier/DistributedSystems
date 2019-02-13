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
          val result = userDao.signup(new User(userName, password))
          Ok(result.get("message"))
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
          if (result.get("code") == "1") {
            val token = encryptor.tokenGenerator()
            return Ok(result.get("message")).withSession(token)

          }
          else {
            return Ok(result.get("message"))
          }


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
