## The Great Gif Catastrophe: A Postmortem

**Issue Summary:**

On Wednesday, August 14th, 2024, between 14:30 and 15:00 WAT (West Africa Time), our internal communication platform experienced a partial outage impacting GIF functionality. Users were unable to upload or share GIFs during this 30-minute window.

**Timeline:**

* **14:30 WAT:**  Monitoring alerts indicated a surge in API errors related to GIF processing.
* **14:32 WAT:** An engineer on duty noticed a significant decrease in successful GIF uploads through the platform.
* **14:35 WAT:** The engineering team investigated the issue, initially suspecting a problem with the storage service responsible for holding uploaded GIFs.
* **14:40 WAT:** Investigation into the storage service revealed no anomalies. Attention shifted towards the API gateway responsible for routing GIF upload requests.
* **14:45 WAT:** A code review of the API gateway identified a recently deployed configuration change that limited file size uploads specifically for GIFs due to a mistaken assumption about file size distribution.
* **14:50 WAT:** The engineering team reverted the configuration change related to GIF uploads.
* **15:00 WAT:** GIF functionality was restored, and all backlog requests were processed successfully.

**Root Cause and Resolution:**

The root cause of the outage was a misconfiguration in the API gateway introduced during a recent deployment. A change intended to limit overall upload file sizes inadvertently restricted GIF uploads due to an oversight in file size distribution analysis. The engineering team promptly identified the issue and reverted the configuration change, restoring full GIF functionality.

**Corrective and Preventative Measures:**

* Implement more granular control over file size limitations within the API gateway to avoid unintended consequences on specific file types.
* Enhance automated testing procedures to include specific scenarios for GIF uploads, ensuring future deployments don't affect this functionality.
* Review code deployment checklists to include a verification step specifically for configuration changes that might impact file handling.

**Lessons Learned:**

This incident highlights the importance of thorough code reviews and comprehensive testing procedures during deployments. Additionally, it emphasizes the value of clear communication and collaboration within the engineering team during troubleshooting. 

##### OHIMAI MATTHEW
