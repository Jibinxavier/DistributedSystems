package controllers

import javax.inject.{Inject, Singleton}
import play.api.mvc.{AbstractController, ControllerComponents}
 
import play.api.libs.json._
// you need this import to have combinators
import play.api.libs.functional.syntax._

class AuthenticationController @Inject()(cc: ControllerComponents,   userDao: UserDao) extends AbstractController(cc) {


  implicit val rds = (
    (__ \ 'name).read[String] and
      (__ \ 'age).read[Long]
    ) tupled
  def signUp = Action { implicit request =>

      if () {
        Ok("Legitamate User")
      }
      else {
        Status(403)("Forbidden")
      }
  }

  def login =  Action {
    Ok("here is your login pager")
  }
  def getUserDetails()
}
