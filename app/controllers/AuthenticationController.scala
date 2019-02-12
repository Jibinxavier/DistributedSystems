package controllers

import javax.inject.{Inject}
import models.{User, UserDBConnector}
import play.api.mvc.{AbstractController, ControllerComponents, Request}


import play.api.libs.json._

class AuthenticationController @Inject()(cc: ControllerComponents,   userDao: UserDBConnector) extends AbstractController(cc) {


  def signUp = Action { request =>
    request.body.asJson.map { json =>
      json.validate[(String, String)].map{
        case (userName, password) =>
          Ok(userDao.signup( new User(userName, password)))
      }.recoverTotal{
        e => BadRequest("Detected error:"+ JsError.toJson(e))
      }
    }.getOrElse {
      BadRequest("Expecting Json data")
    }
  }


  def login = Action { request =>
    request.body.asJson.map { json =>
      json.validate[(String, String)].map{
        case (userName, password) =>

          Ok(userDao.login( new User(userName, password)))
      }.recoverTotal{
        e => BadRequest("Detected error:"+ JsError.toJson(e))
      }
    }.getOrElse {
      BadRequest("Expecting Json data")
    }
  }

}
