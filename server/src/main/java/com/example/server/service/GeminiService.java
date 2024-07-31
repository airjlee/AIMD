package com.example.server.service;

import com.example.server.dto.GeminiRequest;
import com.example.server.dto.GeminiResponse;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class GeminiService {
    private final String PYTHON_SERVICE_URL = "http://localhost:8080/plan";  // Adjust port if needed
    private final RestTemplate restTemplate = new RestTemplate();

    public String generateContent(String prompt) {
        GeminiRequest request = new GeminiRequest(prompt);
        GeminiResponse response = restTemplate.postForObject(PYTHON_SERVICE_URL, request, GeminiResponse.class);
        return response.getGeneratedText();
    }
}
