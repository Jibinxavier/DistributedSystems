name := "DistributedSystems"
 
version := "1.0" 
      
lazy val `distributedsystems` = (project in file(".")).enablePlugins(PlayScala)

resolvers += "scalaz-bintray" at "https://dl.bintray.com/scalaz/releases"
      
resolvers += "Akka Snapshot Repository" at "http://repo.akka.io/snapshots/"
      
scalaVersion := "2.12.2"

libraryDependencies ++= Seq( jdbc , ehcache , ws , specs2 % Test , guice )

unmanagedResourceDirectories in Test <+=  baseDirectory ( _ /"target/web/public/test" )  

val testPythonTask = TaskKey[Unit]("Userdatabase", "Run Python user API.")

val command = "python3 server.py"
val workingDirectory = new File("./database")

testPythonTask := {
  val s: TaskStreams = streams.value
  s.log.info("Executing task Userdatabase")
  Process(command) ! s.log
}