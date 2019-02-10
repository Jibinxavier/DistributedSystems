package controllers

import javax.inject.{Inject}
import models.{User, UserObj}
import play.api.mvc.{AbstractController, ControllerComponents, Request}


import play.api.libs.json._

class AuthenticationController @Inject()(cc: ControllerComponents,   userDao: UserObj) extends AbstractController(cc) {


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
          Ok(userDao.signup( new User(userName, password)))
      }.recoverTotal{
        e => BadRequest("Detected error:"+ JsError.toJson(e))
      }
    }.getOrElse {
      BadRequest("Expecting Json data")
    }
  }

}
