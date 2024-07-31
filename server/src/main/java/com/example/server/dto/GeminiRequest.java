package com.example.server.dto;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;

public class GeminiRequest {
    @Getter
    @Setter
    private String prompt;

    public GeminiRequest(String prompt) {
        this.prompt = prompt;
    }
}