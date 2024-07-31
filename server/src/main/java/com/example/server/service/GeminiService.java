package com.example.server.service;

import org.springframework.stereotype.Service;
import java.io.BufferedReader;
import java.io.InputStreamReader;

@Service
public class GeminiService {
    public String generateContent(String prompt) {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("python", "../../../../../../AIMD/RAG/main.py", prompt);
            Process process = processBuilder.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            StringBuilder output = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

            int exitCode = process.waitFor();
            if (exitCode != 0) {
                throw new RuntimeException("Python script exited with code " + exitCode);
            }

            return output.toString().trim();
        } catch (Exception e) {
            throw new RuntimeException("Error executing Python script", e);
        }
    }
}
