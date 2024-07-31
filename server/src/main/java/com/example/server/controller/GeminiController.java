package com.example.server.controller;

import com.example.server.service.GeminiService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/plan")
public class GeminiController {

    @Autowired
    private final GeminiService geminiService;

    public GeminiController(GeminiService geminiService) {
        this.geminiService = geminiService;
    }

    @PostMapping("/generate")
    public String generateContent(@RequestBody String prompt) {
        return geminiService.generateContent(prompt);
    }
}