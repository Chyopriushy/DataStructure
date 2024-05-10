package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

	@GetMapping(value = "/")
	public String doGetStart(){
		return "20212951 강문경 Spring";
	}

	@GetMapping(value = "/demo")
	public String doGetDemo(){
		return "20212951 강문경 Spring demo";
	}

}
